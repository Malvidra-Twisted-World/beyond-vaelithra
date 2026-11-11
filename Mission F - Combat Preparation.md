---
tags: [DnD, Mission, Combat, DM Only, Homebrew]
campaign: Beyond Vaelithra
mission: F
status: Proposed homebrew for 5 PCs (4 level 3, 1 level 4); not playtested
visibility: DM Only
---

# Mission F — Combat Preparation

[[Mission F Script]] · [[Mission F - VTT Preparation]] · [[Lore/Resonance - Thresholds & Effects Draft]]

> [!important] Status & asumsi
> Semua angka di sini **homebrew usulan**, bukan stat block resmi Mage/Apprentice dan belum playtested. Roster DM: **5 PC — empat level 3 dan satu level 4**, tanpa asumsi mereka memiliki Niskara. Edisi 5e belum dikonfirmasi untuk sesi ini. Skill/stat block tidak menetapkan class level, lisensi atau kemampuan canon jangka panjang NPC.

**Discord / Avrae:** [[Assets/Mission F/Avrae/README - Import to Avrae|CritterDB / Avrae Import Pack]] — JSON bestiary dan panduan import untuk sesi tanpa VTT.

## Encounter yang disiapkan

| Keadaan | Komposisi awal | Tujuan / batas |
|---|---|---|
| Negosiasi berhasil | Tidak ada combat | Rescue tetap resolusi penuh |
| Konflik dengan wizard; roster sesi ini | **Garran + Mara + 1 rekan wizard** | Menghentikan pemindahan equipment; tidak memburu PC/pekerja. Rekan wizard memakai profil ringan di bawah |
| Party kecil / sangat terkuras | Garran sendiri; Mara menolong pekerja | Jangan tambahkan generic wizard |
| Party sesi ini sudah terkuras sebelum konflik | Garran + Mara; rekan wizard mengawal pekerja | Tidak perlu menghabiskan semua caster sebagai lawan |
| Gangguan anomali opsional; roster sesi ini | **3 Unstable Echo** | Gunakan sebagai alternatif fight wizard, bukan tambahan wajib; turunkan menjadi 2 jika party sudah terkuras |

Untuk level 1–2, jangan memakai baseline ini tanpa penyesuaian lagi. Cek sumber daya party dan kemampuan homebrew sebelum menambah lawan. Profil ini mengutamakan negosiasi dan ekstraksi; bukan boss battle dengan ancaman TPK yang disengaja. Tidak ada CR/XP encounter yang diklaim terhitung di sini.

**Combat mulai setelah ancaman atau tindakan nyata party**, bukan karena gagal satu Persuasion check. Semua pihak tetap boleh bicara, melepaskan equipment, mundur, atau mencari kesepakatan di tengah initiative. Hindari AoE ke kumpulan enam pekerja.

## Garran Vey — containment caster

```statblock
layout: Basic 5e Layout
name: Garran Vey
source: Beyond Vaelithra (Homebrew)
size: Medium
type: Humanoid (Human)
ac: 13
hp: 44
speed: 30 ft.
stats: [10, 12, 14, 16, 13, 12]
saves:
  - INT: 5
  - WIS: 3
skillsaves:
  - Arcana: 5
  - Insight: 3
  - Persuasion: 3
senses: Passive Perception 11
languages: Common
actions:
  - name: Arcane Bolt
    desc: "Ranged Spell Attack: +5 to hit, range 60 ft., one target Garran can see. Hit: 10 (2d6 + 3) force damage."
  - name: Binding Field (2/Encounter)
    desc: "Garran creates a field of arcane force around one creature he can see within 30 feet of him. The target must succeed on a DC 13 Strength saving throw or have its speed reduced to 0 until the end of Garran's next turn. The target can use its action to repeat the saving throw, ending the effect on itself on a success. This effect requires no concentration, and multiple uses of Binding Field on the same target do not stack."
  - name: Staff
    desc: "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 3 (1d6) bludgeoning damage."
reactions:
  - name: Containment Ward (2/Encounter)
    desc: "When Garran or an ally he can see within 30 feet of him takes damage, Garran conjures a protective ward, reducing that damage by 1d6 + 2, to a minimum of 0. Garran uses this reaction after the damage is determined. The ward does not prevent any other effects associated with the damage."
```

**Taktik:** Mulai dengan Binding Field terhadap pengangkut equipment; gunakan bolt bila benar-benar diserang. Binding tidak memaksa target menyerahkan barang. Di **HP 16 atau kurang**, Garran menawarkan ceasefire pada kesempatan bicara berikutnya; ini perilaku, bukan reaction tambahan. Ancaman kepada pekerja atau fasilitas kolaps dapat membuatnya berhenti lebih cepat. Ia tidak menyerang PC downed dan tidak bertarung sampai mati.

## Mara Vell — apprentice support

```statblock
layout: Basic 5e Layout
name: Mara Vell
source: Beyond Vaelithra (Homebrew)
size: Medium
type: Humanoid (Half-Elf)
ac: 12
hp: 22
speed: 30 ft.
stats: [8, 14, 12, 14, 12, 11]
saves:
  - INT: 4
skillsaves:
  - Arcana: 4
  - Insight: 3
senses: Passive Perception 11
languages: Common, Elvish
actions:
  - name: Spark
    desc: "Ranged Spell Attack: +4 to hit, range 60 ft., one target Mara can see. Hit: 6 (1d8 + 2) lightning damage."
  - name: Repelling Gesture (2/Encounter)
    desc: "Mara directs a pulse of magical force at one creature she can see within 30 feet of her. The target must succeed on a DC 12 Strength saving throw or be pushed 5 feet away from Mara."
  - name: Staff
    desc: "Melee Weapon Attack: +1 to hit, reach 5 ft., one target. Hit: 2 (1d6 − 1) bludgeoning damage (minimum 0 damage)."
```

**Taktik:** Membantu pekerja mencari cover dan mencoba menengahi. Mara menghindari Spark terhadap target yang tampak hampir jatuh dan memakai Repelling Gesture hanya jika target memiliki ruang aman untuk terdorong, bukan ke tepi jurang atau runtuhan. Di **HP 8 atau kurang**, Mara mundur atau menyerah. Ia dapat menolak perintah Garran yang membahayakan pekerja, tanpa membuat negosiasi menjadi kemenangan otomatis.

## Rekan Wizard — opsional, token Wizard Generic

```statblock
layout: Basic 5e Layout
name: Wizard Associate
source: Beyond Vaelithra (Homebrew)
size: Medium
type: Humanoid
ac: 12
hp: 16
speed: 30 ft.
stats: [10, 12, 12, 13, 11, 10]
skillsaves:
  - Arcana: 3
senses: Passive Perception 10
languages: Common
actions:
  - name: Arcane Dart
    desc: "Ranged Spell Attack: +3 to hit, range 60 ft., one target the wizard can see. Hit: 5 (1d6 + 2) force damage."
```

**Catatan DM:** Wizard Associate memakai token Wizard Generic; profil ini tidak menambahkan NPC bernama baru.

**Taktik:** Menyerah/mundur ketika Garran berhenti atau HP ≤ 5. Jangan menambah jumlahnya hanya karena tersedia token generik.

## Unstable Echo — opsi monster, belum canon

> [!warning] Tambahan opsional untuk persetujuan DM
> Script belum menetapkan monster. **Unstable Echo** adalah usulan bentuk energi tak stabil sementara di corridor, tanpa memastikan sumber atau kesadarannya. Memakainya tidak membuktikan ada makhluk keluar dari Sealed Chamber. Jangan tampilkan jika DM memilih rescue tanpa monster. Token monster belum dibuat dalam paket VTT; sementara gunakan marker abstrak bercahaya bertuliskan Echo 1/2.

Nama monster ini tidak berarti ia adalah **Echo perkenalan Resonansi**. Efek perkenalan adalah marker modifier PC, bukan creature yang dipanggil atau dimiliki PC. Untuk tiga monster, gunakan marker Echo 1/2/3.

```statblock
layout: Basic 5e Layout
name: Unstable Echo
source: Beyond Vaelithra (Homebrew)
size: Small
type: Construct
ac: 12
hp: 18
speed: 25 ft.
stats: [6, 14, 12, 3, 10, 5]
damage_immunities: poison
condition_immunities: Poisoned
senses: Passive Perception 10
languages: "—"
traits:
  - name: Unstable Pattern
    desc: "A creature that can see the echo within 30 feet of itself can use its action to make a DC 12 Intelligence (Arcana) check, disrupting the echo's pattern on a success. After the first successful check, the echo visibly flickers and dims. After the second successful check, the echo dissipates. The successes can come from different creatures, and a failed check does not remove any successes."
actions:
  - name: Arc Discharge
    desc: "Ranged Spell Attack: +4 to hit, range 30 ft., one target the echo can see. Hit: 5 (1d6 + 2) force damage."
  - name: Flicker Burst (1/Encounter)
    desc: "The echo releases a pulse of unstable energy at a point it can see within 30 feet of itself that is not behind total cover. Each creature in a 5-foot-radius sphere centered on that point must make a DC 12 Dexterity saving throw, taking 3 (1d6) force damage on a failed save, or no damage on a successful one."
```

**Catatan DM:** Tipe Construct hanya untuk aturan targeting, bukan penetapan pembuat atau asal Echo. Gunakan penglihatan dan pendengaran normal 60 ft.; token menempati 1 kotak dan tidak menembus dinding atau creature lain. Hindari menaruh Flicker Burst di kerumunan pekerja.

### Alternatif menonaktifkan

Creature dalam 30 ft yang bisa melihat Echo dapat memakai **Action, Arcana DC 12** untuk mendestabilkan polanya. **Dua sukses total terhadap Echo yang sama** membuatnya lenyap tanpa damage; kegagalan tidak mereset sukses. Sukses pertama terlihat jelas sebagai kedipan yang melemah. PC boleh bergantian. Tidak membutuhkan notebook, scanner atau spell tertentu. Serangan biasa tetap alternatif sah.

**Pemicu usulan:** sesudah peringatan visual/suara yang jelas saat extraction, terutama bila DM ingin party dan wizard bekerja sama. Wujudnya tidak menyerang hanya karena seseorang gagal check Resonansi atau memilih Sin tertentu. Tidak memberi poin Resonansi otomatis saat dikalahkan.

## Enam surveyor — rescue profile

Untuk **Bram, Yara dan Surveyor 03–06**, gunakan profil yang sama berikut. Ini penyederhanaan encounter, bukan character sheet final; mereka tidak memiliki serangan rutin atau giliran ofensif yang perlu dikelola DM. Trait Death Saving Throws merupakan house rule rescue usulan.

```statblock
layout: Basic 5e Layout
name: Surveyor
source: Beyond Vaelithra (Homebrew)
ac: 10
hp: 9
speed: 30 ft.
stats: [10, 10, 10, 10, 10, 10]
traits:
  - name: Death Saving Throws
    desc: "When the surveyor is reduced to 0 hit points, the surveyor falls unconscious and makes death saving throws as a player character would."
```

- Satu initiative bersama; ikuti instruksi evakuasi yang masuk akal, gunakan **Dash** di jalur aman atau **Dodge** saat menunggu. Pekerja sadar tidak memerlukan Action PC setiap giliran untuk sekadar berjalan.
- PC tetap perlu mempertimbangkan pintu, kepanikan, pekerja downed dan jalur yang benar-benar tersedia. Bukan NPC yang teleport mengikuti party.
- Sebagai **house rule rescue usulan**, pekerja di 0 HP memakai death saves seperti PC; tidak langsung dianggap mati. Jangan menargetkan mereka demi memaksa hasil partial/failure.
- Tidak ada penalti Exhaustion yang ditambahkan hanya karena deskripsi mereka lelah.

## Menghentikan pertarungan

1. Tanyakan tawaran nyata kedua pihak saat situasi berubah; initiative tidak menutup negosiasi.
2. Jika Garran menghentikan penahanan, jangan teruskan fight untuk menghabiskan HP lawan. Catat siapa menyimpan equipment dan siapa mengawal pekerja.
3. Jika menggunakan Echo, izinkan wizard membantu ekstraksi; jangan sekaligus menjadikan mereka penyerang PC tanpa alasan baru.
4. Jangan menumpuk **monster + wizard + damaging hazard** di ronde yang sama sebagai paket default. Untuk sesi awal, pilih satu sumber tekanan utama; hazard ringan dapat berupa pintu tertutup tanpa damage.

### Reference aturan dasar

Profil dan powers di atas ditulis sendiri sebagai homebrew. Attack rolls, saving throws, aksi dasar dan aturan menjatuhkan lawan tanpa membunuh mengikuti edisi yang dipakai meja. **Ranged spell attack tidak otomatis nonlethal**; gunakan Staff/melee dan aturan knockout edisi meja bila ingin menahan seseorang.

Rujukan resmi yang diperiksa: [D&D Free Rules 2024 — Playing the Game](https://www.dndbeyond.com/sources/dnd/br-2024/playing-the-game) dan [Basic Rules 2014 — Combat](https://www.dndbeyond.com/sources/dnd/basic-rules-2014/combat). Rujukan ini tidak mengonfirmasi edisi campaign dan bukan sumber angka stat block homebrew ini.
