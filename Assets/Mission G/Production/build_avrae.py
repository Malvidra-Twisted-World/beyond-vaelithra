"""Rebuild Mission G CritterDB and Avrae presets from the canonical statblocks."""
from pathlib import Path
import ast, json, math, re, subprocess
from urllib.parse import quote
ROOT = Path(__file__).resolve().parents[1]
CAMPAIGN = ROOT.parents[1]
OUT = ROOT/'Avrae'
MAPS = OUT/'Map Templates'
BASE = 'https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/'

def raw_url(path):
    return BASE + quote(path.relative_to(CAMPAIGN).as_posix())

def build():
    ruby = 'require "json"; require "yaml"; STDOUT.write(JSON.generate(STDIN.read.scan(/```statblock\\n(.*?)\\n```/m).flatten.map { |b| YAML.safe_load(b) }))'
    parsed = subprocess.run(['ruby','-E','UTF-8','-e',ruby],input=(CAMPAIGN/'Mission G - Combat Preparation.md').read_text(),text=True,capture_output=True,check=True)
    blocks = json.loads(parsed.stdout)
    assert len(blocks)==4
    abilities=['strength','dexterity','constitution','intelligence','wisdom','charisma']
    shorts=dict(zip(['STR','DEX','CON','INT','WIS','CHA'],abilities))
    tokens={'Ratri Sembada':'Ratri-Sembada.png','Recovery Hand':'Recovery-Hand.png','Packing Sentinel':'Packing-Sentinel.png','Damar Seta':'Damar-Seta.png'}
    creatures=[]
    for b in blocks:
        name=b['name']; m=re.fullmatch(r'(\d+)d(\d+)(?:\s*\+\s*(\d+))?',b['hit_dice']);assert m
        n,d=int(m[1]),int(m[2]);scores=dict(zip(abilities,b['stats']))
        hp=math.floor(n*(d+1)/2)+n*((scores['constitution']-10)//2);assert hp==b['hp']
        assert int(m[3] or 0)==n*((scores['constitution']-10)//2)
        stats={'size':b['size'],'race':b['type'],'alignment':'','armorType':'','armorClass':b['ac'],'numHitDie':n,'hitDieSize':d,'speed':b['speed'],'abilityScores':scores,'proficiencyBonus':2,
               'savingThrows':[{'ability':shorts[k],'value':v,'proficient':False} for row in b.get('saves',[]) for k,v in row.items()],
               'skills':[{'name':k,'value':v,'proficient':False} for row in b.get('skillsaves',[]) for k,v in row.items()],
               'damageVulnerabilities':[],'damageResistances':[], 'damageImmunities':[x.strip() for x in b.get('damage_immunities','').split(',') if x.strip()],
               'conditionImmunities':[x.strip() for x in b.get('condition_immunities','').split(',') if x.strip()],
               'senses':[], 'languages':[b['languages']], 'challengeRating':0,'experiencePoints':0,
               'additionalAbilities':[], 'actions':[], 'reactions':[], 'legendaryActionsPerRound':0,'legendaryActionsDescription':'','legendaryActions':[]}
        for key,dest in [('traits','additionalAbilities'),('actions','actions'),('reactions','reactions')]:
            stats[dest]=[{'name':x['name'],'description':x['desc']} for x in b.get(key,[])]
        creatures.append({'name':name,'flavor':{'nameIsProper':name in ('Ratri Sembada','Damar Seta'),'faction':'','environment':'The Fringe','description':'Beyond Vaelithra — Mission G. Proposed homebrew encounter profile; not played or CR-balanced. CR 0 / XP 0 are import placeholders. Special effects and encounter uses require manual tracking.','imageUrl':raw_url(ROOT/'Tokens'/tokens[name])},'stats':stats})
    OUT.mkdir(exist_ok=True);MAPS.mkdir(exist_ok=True)
    (OUT/'Mission G - CritterDB Bestiary.json').write_text(json.dumps({'name':'Beyond Vaelithra — Mission G','description':'Mission #037, The Empty Lair. Four proposed homebrew profiles; no naga profile or plot answers. CR/XP are unassessed import placeholders.','creatures':creatures},ensure_ascii=False,indent=2)+'\n')
    scenes={'g1':'G1-Utility-Cut.png','g2':'G2-Receiving-Hall.png','g3':'G3-Archive-Packing.png','g4':'G4-Dispatch-Bay.png'}
    urls={k:raw_url(ROOT/'Maps'/v) for k,v in scenes.items()}
    scene='''<drac2>
c = combat()
if not c:
    err("Start initiative with !init begin first.")
a = &ARGS&
s = a[0].lower() if a else "g1"
urls = URLS
if s not in urls:
    err("Use !mgscene g1, g2, g3, or g4.")
u = get("mg_map_" + s, urls[s])
if not u.startswith("https://") or any(x in u for x in ['"', "~", "\\n", " "]):
    err("Set a direct HTTPS image URL: !uvar mg_map_" + s + " URL")
dm = c.get_combatant("DM", strict=True)
cmds = []
if not dm:
    cmds.append("!init add 0 DM -p 20")
elif dm.get_effect("map", strict=True):
    cmds.append("!init re DM map")
cmds.append('!init effect DM map -attack "||Size: 24x16 ~ Background: ' + u + ' ~ Options: c64"')
return "multiline\\n" + "\\n".join(cmds)
</drac2>'''.replace('URLS',repr(urls))
    header='''<drac2>
c = combat()
if not c:
    err("Start initiative with !init begin first.")
a = &ARGS&
p = a[0] if a else "4"
if p not in ["2", "3", "4", "5"]:
    err("Pass party size 2, 3, 4, or 5.")
p = int(p)
'''
    crew=header+'''roster = [["Ratri Sembada", "RS", "H7", "p", 18 if p == 2 else 27]]
if p >= 3:
    roster.append(["Recovery Hand", "RH1", "R7", "o", 11])
if p == 5:
    roster.append(["Recovery Hand", "RH2", "H11", "o", 11])
'''
    sentinel=header+'''hp = 14 if p == 2 else 16 if p == 4 else 22
roster = [["Packing Sentinel", "PS1", "H10", "c", hp]]
if p >= 4:
    roster.append(["Packing Sentinel", "PS2", "R10", "c", hp])
'''
    tail='''cmds = []
for monster, name, loc, color, hp in roster:
    if not c.get_combatant(name, strict=True):
        cmds.append('!init madd "' + monster + '" -name "' + name + '" -hp ' + str(hp) + ' -note "Location: ' + loc + ' | Size: M | Color: ' + color + '"')
return "multiline\\n" + "\\n".join(cmds) if cmds else 'echo Preset already present; HP and positions were preserved.'
</drac2>'''
    aliases={'mgscene':scene,'mgcrew':crew+tail,'mgsentinel':sentinel+tail}
    aliases={key:body.replace(chr(92)*2+'n',chr(92)+'n') for key,body in aliases.items()}
    for alias,body in aliases.items():
        install='!alias '+alias+' '+body+'\n';assert len(install)<2000
        (MAPS/(alias+' - install.txt')).write_text(install)
    (MAPS/'Mission G - Map Presets.json').write_text(json.dumps({'grid':{'columns':24,'rows':16,'cellPixels':64,'feetPerCell':5},'mapFiles':scenes,'publicMapUrls':urls,'discordTested':False,'notes':'Only load crew/sentinel after narration. Mutually exclusive combat pressure. Scene switches preserve HP and token notes.'},indent=2)+'\n')
    (MAPS/'Mission G - uvars.txt').write_text('\n\n'.join('!uvar mg_map_'+k+' '+url for k,url in urls.items())+'\n')
    print('Built 4 CritterDB profiles, 3 installable aliases, 4 uvar commands.')
    return blocks,aliases

if __name__=='__main__':build()
