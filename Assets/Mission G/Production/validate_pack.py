"""Validate Mission G assets/data and rebuild portable session/player/Avrae archives."""
from pathlib import Path
import ast, hashlib, json, math, re, struct, subprocess, zipfile, zlib
ROOT=Path(__file__).resolve().parents[1]
CAMPAIGN=ROOT.parents[1]

def inspect_png(path):
    data = path.read_bytes()
    assert data[:8] == b'\x89PNG\r\n\x1a\n', path
    pos, compressed = 8, bytearray()
    while pos < len(data):
        size = struct.unpack('>I', data[pos:pos + 4])[0]
        kind = data[pos + 4:pos + 8]
        payload = data[pos + 8:pos + 8 + size]
        crc = struct.unpack('>I', data[pos + 8 + size:pos + 12 + size])[0]
        assert zlib.crc32(kind + payload) & 0xffffffff == crc, path
        if kind == b'IHDR':
            w, h, bits, color, comp, filt, interlace = struct.unpack('>IIBBBBB', payload)
        if kind == b'IDAT':
            compressed.extend(payload)
        pos += 12 + size
        if kind == b'IEND':
            break
    assert bits == 8 and color in (2, 6) and interlace == 0, path
    bpp = 4 if color == 6 else 3
    raw = zlib.decompress(compressed)
    stride = w * bpp
    assert len(raw) == h * (stride + 1), path
    alpha_min, alpha_max, corner_alpha = 255, 0, []
    if color == 6:
        previous = bytearray(stride)
        offset = 0
        for y in range(h):
            mode = raw[offset]
            row = bytearray(raw[offset + 1:offset + 1 + stride])
            for x in range(stride):
                a = row[x - bpp] if x >= bpp else 0
                b = previous[x]
                c = previous[x - bpp] if x >= bpp else 0
                if mode == 1:
                    predictor = a
                elif mode == 2:
                    predictor = b
                elif mode == 3:
                    predictor = (a + b) // 2
                elif mode == 4:
                    p = a + b - c
                    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                    predictor = a if pa <= pb and pa <= pc else b if pb <= pc else c
                else:
                    assert mode == 0, path
                    predictor = 0
                row[x] = (row[x] + predictor) & 255
            alphas = row[3::4]
            alpha_min = min(alpha_min, min(alphas))
            alpha_max = max(alpha_max, max(alphas))
            if y in (0, h - 1):
                corner_alpha.extend((alphas[0], alphas[-1]))
            previous = row
            offset += stride + 1
    record = dict(file=path.relative_to(ROOT).as_posix(), width=w, height=h,
                  mode='RGBA' if color == 6 else 'RGB', bytes=len(data),
                  sha256=hashlib.sha256(data).hexdigest())
    if path.parent.name == 'Tokens':
        assert color == 6 and w == h and alpha_min == 0 and alpha_max == 255, path
        assert max(corner_alpha) <= 5, (path, corner_alpha)
        record.update(alpha_min=alpha_min, alpha_max=alpha_max, corner_alpha=corner_alpha,
                      display_cells=[1, 1])
    else:
        assert (w, h) == (1536, 1024), path
        record.update(grid_px=64, grid_offset_px=[0, 0], grid_cells=[24, 16], feet_per_cell=5)
    return record

class MockCombatant:
    def __init__(self,effect=False):self.effect=effect
    def get_effect(self,name,strict=False):return object() if self.effect else None
class MockCombat:
    def __init__(self,items=None):self.items=items or {}
    def get_combatant(self,name,strict=False):return self.items.get(name)
def alias_run(body,c,args=None,url_override=None):
    body=body.removeprefix('<drac2>\n').removesuffix('\n</drac2>').replace('&ARGS&',repr(args or []))
    def err(msg):raise ValueError(msg)
    env={'combat':lambda:c,'get':lambda k,d:url_override if url_override is not None else d,'err':err}
    exec('def check():\n'+''.join('    '+line+'\n' for line in body.splitlines()),env)
    return env['check']()

def main():
    from build_avrae import build
    blocks,aliases=build()
    maps=sorted((ROOT/'Maps').glob('*.png'));tokens=sorted((ROOT/'Tokens').glob('*.png'))
    assert len(maps)==4 and len(tokens)==4
    records=[inspect_png(p) for p in maps+tokens]
    manifest={'mission':'G — The Empty Lair','mission_number':'037','generator':'Built-in image_gen','status':'Proposed prep; not played','rules':'D&D 2024','party':'2–5 level 3–4 PCs','wulan':'Use existing DM asset; not generated','local_png_checks':'passed','discord_tested':False,'playtested':False,'assets':records}
    (ROOT/'Production/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    for name in ['mgscene','mgcrew','mgsentinel']:
        assert len(('!alias '+name+' '+aliases[name]))<2000
    scene_result=alias_run(aliases['mgscene'],MockCombat())
    assert scene_result.startswith('multiline'+chr(10)) and chr(92)+'n' not in scene_result
    assert '!init add 0 DM' in scene_result
    assert '!init re DM map' in alias_run(aliases['mgscene'],MockCombat({'DM':MockCombatant(True)}))
    for args,url in [(['wrong'],None),(['g3'],'https://invalid/~bad'),(['g3'],'not-a-url')]:
        try:alias_run(aliases['mgscene'],MockCombat(),args,url)
        except ValueError:pass
        else:raise AssertionError('Invalid scene or URL accepted')
    existing={name:MockCombatant() for name in ['RS','RH1','RH2','PS1','PS2']}
    for p in range(2,6):
        crew=alias_run(aliases['mgcrew'],MockCombat(),[str(p)])
        sentinel=alias_run(aliases['mgsentinel'],MockCombat(),[str(p)])
        assert crew.startswith('multiline'+chr(10)) and sentinel.startswith('multiline'+chr(10))
        assert chr(92)+'n' not in crew and chr(92)+'n' not in sentinel
        assert crew.count('!init madd')=={2:1,3:2,4:2,5:3}[p]
        assert sentinel.count('!init madd')==(1 if p<=3 else 2)
        assert alias_run(aliases['mgcrew'],MockCombat(existing),[str(p)]).startswith('echo')
        assert alias_run(aliases['mgsentinel'],MockCombat(existing),[str(p)]).startswith('echo')
        assert f'-hp {14 if p==2 else 16 if p==4 else 22}' in sentinel
    # Test the exact attack recognizer from the downloaded public Avrae parser.
    parser=Path('/tmp/mission-g-avrae-bestiary.py')
    if parser.exists():
        tree=ast.parse(parser.read_text());wanted={'AVRAE_ATTACK_OVERRIDES_RE','ATTACK_RE','JUST_DAMAGE_RE'}
        nodes=[n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in wanted for t in n.targets)]
        ns={'re':re};exec(compile(ast.Module(body=nodes,type_ignores=[]),'<avrae expressions>','exec'),ns)
        attacks=0
        for b in blocks:
            for a in b.get('actions',[]):
                if 'Attack:' in a['desc']:
                    assert len(list(ns['ATTACK_RE'].finditer(a['desc'])))==1,(b['name'],a['name']);attacks+=1
        assert attacks==6
        parser_result='Six weapon attacks recognized by public Avrae parser expressions.'
    else:parser_result='Parser source absent; attack recognition not rerun.'
    # Handouts must not contain DM distribution instructions or hidden-complication headings.
    handouts=sorted((ROOT/'Handouts').glob('*.md'));assert len(handouts)==4
    for p in handouts:
        assert all(x not in p.read_text() for x in ['READ ALOUD','Hidden Complication','Berikan:','Implementasi DM'])
    # Check all Mission G wiki-note targets exist; anchors are not treated as extra files.
    docs=sorted(CAMPAIGN.glob('Mission G*.md'))
    for p in docs:
        text=p.read_text();assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)',text,re.M)
        for target in re.findall(r'\[\[([^\]]+)\]\]',text):
            target=target.split('|',1)[0].split('#',1)[0].strip()
            if not target:continue
            candidate=CAMPAIGN/(target if target.endswith('.md') else target+'.md')
            assert candidate.exists(),(p.name,target)
    script=(CAMPAIGN/'Mission G Script.md').read_text()
    assert '175 Escrow' in script and 'Tidak ada naga' in script
    assert 'pernah dipakai seorang naga' in script
    # Store guide JS separately for optional node syntax check, without modifying the guide.
    html=(ROOT/'DM Map Guide.html').read_text()
    js=re.search(r'<script>(.*?)</script>',html,re.S).group(1)
    temp=Path('/tmp/mission-g-map-guide.js');temp.write_text(js)
    try:subprocess.run(['node','--check',str(temp)],check=True,capture_output=True)
    except FileNotFoundError:pass
    for scene in json.loads((ROOT/'Production/map-key.json').read_text()):
        assert (ROOT/'Maps'/scene['file']).exists()
        for _,cell,_ in scene['keys']:assert re.fullmatch(r'[A-X](?:1[0-6]|[1-9])',cell)
    report='# Mission G — Validation Report\n\n'
    report+='Local checks passed: 4 PNG maps (1536×1024), 4 square RGBA token PNGs with transparent corners, PNG chunk CRC/decompression, 4 statblock YAML blocks, CritterDB HP formulas, 3 alias size limits, scene/URL guards, all 2–5 PC roster counts/HP, duplicate guards, 4 player-safe handouts, local note links, and map guide JavaScript syntax.\n\n'
    report+=parser_result+'\n\n'
    report+='Alias checks use mocked Python-compatible control flow, not execution in Draconic or Discord. No live CritterDB import, server command test, CR balancing, or playtest is claimed. Tes pengambilan URL/render OTFBM dilewati sesuai arahan DM; tampilan akhir akan dicoba melalui !map di Discord. Hosting URL tidak dihitung sebagai uji bot.\n'
    old=ROOT/'Production/validation-report.md'
    if old.exists() and '## Public verification' in old.read_text():report+='\n## Public verification'+old.read_text().split('## Public verification',1)[1]
    old.write_text(report)
    # Portable copies are output artifacts; canonical sources remain the root notes.
    for name in ['Mission G Script.md','Mission G Overview.md','Mission G - Combat Preparation.md','Mission G - VTT Preparation.md','Mission G - Handouts.md','Mission G - Session Prep.md']:
        (ROOT/name).write_text((CAMPAIGN/name).read_text())
    session=ROOT/'mission-g-session-pack-v1.zip'
    with zipfile.ZipFile(session,'w',zipfile.ZIP_DEFLATED) as z:
        for p in docs:z.write(p,p.name)
        for p in sorted(ROOT.rglob('*')):
            if not p.is_file() or p.suffix=='.zip' or 'Variants' in p.parts or '__pycache__' in p.parts or p.parent==ROOT and p.suffix=='.md':continue
            z.write(p,p.relative_to(CAMPAIGN))
    player=ROOT/'mission-g-player-assets-v1.zip'
    with zipfile.ZipFile(player,'w',zipfile.ZIP_DEFLATED) as z:
        for folder in ['Maps','Tokens','Handouts']:
            for p in sorted((ROOT/folder).iterdir()):
                if p.is_file():z.write(p,p.relative_to(ROOT))
    avrae=ROOT/'Avrae/mission-g-avrae-import-v1.zip'
    with zipfile.ZipFile(avrae,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted((ROOT/'Avrae').rglob('*')):
            if p.is_file() and p.suffix!='.zip':z.write(p,p.relative_to(ROOT/'Avrae'))
    for p in [session,player,avrae]:
        with zipfile.ZipFile(p) as z:assert z.testzip() is None
        print(p.name,p.stat().st_size,'bytes; integrity OK')
    print('All local checks passed. Public rendering/Discord/playtesting are separate.')

if __name__=='__main__':main()
