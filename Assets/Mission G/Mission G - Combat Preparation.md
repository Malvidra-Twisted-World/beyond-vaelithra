---
tags: [DnD, Mission, Combat, Homebrew, DM Only]
mission: G
rules: D&D 2024
status: Proposed homebrew; not playtested or CR-balanced
visibility: DM Only
---

# Mission G — Combat Preparation

[[Mission G Script]] · [[Mission G Overview]] · [[Mission G - VTT Preparation]]

> [!important] Encounter assumptions
> **2–5 fixer level 3–4; roster aktual belum dipilih.** Semua profil adalah homebrew encounter, bukan statblock resmi atau class level NPC. Aturan meja memakai 2024; deskripsi serangan berbahasa Inggris mengikuti bentuk yang dapat dibaca Fantasy Statblocks dan parser CritterDB/Avrae. CR/XP belum dihitung. Limited use reset **per encounter**, bukan per day.

## Pilih roster sesuai keadaan

| Party | Jika crew benar-benar melawan | Jika alat diaktifkan |
|---|---|---|
| 2 PC level 3 | Ratri sendiri, **HP 18**; helper mengamankan jalur | 1 Sentinel, **HP 14** |
| 3 PC level 3 | Ratri + 1 Recovery Hand | 1 Sentinel, HP 22 |
| 4 PC level 3–4 | Ratri + 1 Recovery Hand | 2 Sentinel, **HP 16 masing-masing** |
| 5 PC level 3–4 | Ratri + 2 Recovery Hand | 2 Sentinel, HP 22 masing-masing |
| Party terkuras | Kurangi helper atau gunakan baseline 2 PC | 1 Sentinel HP 14, latch jelas terlihat |

Ini **usulan scaling, bukan hitungan encounter resmi**. Resource, Action economy, dan homebrew PC mengubah ancaman. Jangan mengklaim easy/deadly terhitung. High Risk pada board berasal dari informasi parsial dan dugaan pemilik kuat, bukan janji naga/TPK.

**Pakai crew ATAU sentinel**, jangan dua roster menyerang sekaligus. Jangan menambah damaging hazard sebagai tekanan ketiga. Kehadiran sosial beberapa helper tidak mewajibkan semuanya mendapat giliran ofensif.

## Ratri Sembada

```statblock
layout: Basic 5e Layout
name: Ratri Sembada
source: Beyond Vaelithra (Homebrew)
image: D&D/Original Adventures/Vaelithra/Beyond Vaelithra Adventures/Assets/Mission G/Tokens/Ratri-Sembada.png
size: Medium
type: Humanoid (Human)
ac: 13
hp: 27
hit_dice: 5d8 + 5
speed: 30 ft.
stats: [10, 14, 12, 12, 13, 14]
saves:
  - DEX: 4
  - WIS: 3
skillsaves:
  - Investigation: 3
  - Insight: 3
  - Survival: 3
  - Persuasion: 4
senses: Passive Perception 11
languages: Common
actions:
  - name: Survey Bolt
    desc: "Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 5 (1d6 + 2) piercing damage."
  - name: Light Baton
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage."
reactions:
  - name: Fall Back (1/Encounter)
    desc: "When an ally Ratri can see within 30 feet of her is reduced to 0 hit points, Ratri moves up to 10 feet without provoking Opportunity Attacks."
```

**Taktik:** Meminta jarak dan menawarkan jalan keluar; Dodge/Disengage bila tujuan dapat tercapai tanpa melukai PC. Survey Bolt hanya ketika benar-benar diserang; ranged damage tidak otomatis nonlethal. Tidak ada Multiattack, spell slot, atau resistance khusus.

**Morale:** pada HP **10 atau kurang**, menawarkan ceasefire/menyerah. Juga berhenti jika bukti K-17 meyakinkan, helper jatuh, atau ada jalan mundur. Ini perilaku, bukan Reaction tambahan.

## Recovery Hand

```statblock
layout: Basic 5e Layout
name: Recovery Hand
source: Beyond Vaelithra (Homebrew)
image: D&D/Original Adventures/Vaelithra/Beyond Vaelithra Adventures/Assets/Mission G/Tokens/Recovery-Hand.png
size: Medium
type: Humanoid
ac: 12
hp: 11
hit_dice: 2d8 + 2
speed: 30 ft.
stats: [12, 12, 12, 10, 10, 10]
skillsaves:
  - Athletics: 3
senses: Passive Perception 10
languages: Common
actions:
  - name: Baton
    desc: "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) bludgeoning damage."
  - name: Hand Crossbow
    desc: "Ranged Weapon Attack: +3 to hit, range 30/120 ft., one target. Hit: 4 (1d6 + 1) piercing damage."
```

Generic worker, bukan NPC bernama baru. **Mundur pada HP ≤4** atau saat Ratri berhenti. Tidak menarget PC downed. Tidak ada Multiattack, save proficiency, atau resistance khusus. Gunakan Help/Disengage untuk mengawal rekan; memiliki token tidak mewajibkan menyerang.

## Packing Sentinel

```statblock
layout: Basic 5e Layout
name: Packing Sentinel
source: Beyond Vaelithra (Homebrew)
image: D&D/Original Adventures/Vaelithra/Beyond Vaelithra Adventures/Assets/Mission G/Tokens/Packing-Sentinel.png
size: Medium
type: Construct
ac: 13
hp: 22
hit_dice: 4d8 + 4
speed: 20 ft.
stats: [14, 10, 12, 3, 10, 3]
damage_immunities: poison
condition_immunities: Charmed, Frightened, Poisoned
senses: Passive Perception 10
languages: Understands simple handling commands in Common but can't speak
traits:
  - name: Handling Circuit
    desc: "The sentinel is inactive while its handling circuit is switched off. Switching the circuit off immediately ends any effect of the sentinel's Hold Position action."
  - name: Shutdown Latch
    desc: "A creature within 5 feet of the sentinel can take an action to make a DC 12 Dexterity check using Thieves' Tools or a DC 12 Intelligence (Arcana) check. On a success, the sentinel becomes inactive until its handling circuit is deliberately switched on again. A failed check has no additional effect."
actions:
  - name: Padded Clamp
    desc: "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 5 (1d6 + 2) bludgeoning damage."
  - name: Hold Position (2/Encounter)
    desc: "The sentinel directs its handling field at one creature it can see within 15 feet of itself. The target must succeed on a DC 12 Strength saving throw or have its Speed reduced to 0 until the end of the sentinel's next turn. The target can still act normally. The effect ends early if the sentinel becomes inactive or is destroyed."
```

**Dormansi awal:** mati, tanpa turn ofensif, tidak menyerang karena K-17 dibuka/dibawa. Beri warning lampu, rel, dan clamp sebelum alat bekerja. Hanya aktivasi handling menyalakannya.

**Shutdown lain:** panel G2 dapat dikembalikan OFF dengan **Action tanpa check**, mematikan seluruh circuit. Dua unit dapat dimatikan lewat latch masing-masing atau circuit bersama. Hanya ON yang disengaja dapat menyalakan ulang; memindahkan barang tidak menekan ON.

**Batas ruang:** tidak menembus trolley/tembok dan tidak mengejar keluar G4. Tidak punya resistance nonmagical, AoE, atau retaliation saat shutdown gagal. Token satu kotak; mesin besar dalam dressing gambar bukan token Huge.

## Damar Seta — fallback civilian profile

```statblock
layout: Basic 5e Layout
name: Damar Seta
source: Beyond Vaelithra (Homebrew)
image: D&D/Original Adventures/Vaelithra/Beyond Vaelithra Adventures/Assets/Mission G/Tokens/Damar-Seta.png
size: Medium
type: Humanoid (Human)
ac: 10
hp: 9
hit_dice: 2d8
speed: 30 ft.
stats: [10, 10, 10, 12, 11, 12]
skillsaves:
  - Investigation: 3
  - Persuasion: 3
senses: Passive Perception 10
languages: Common
actions:
  - name: Improvised Strike
    desc: "Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage."
```

Damar tidak menemani ekspedisi atau menjadi boss kejutan. Profil hanya fallback bila situasi membutuhkan angka; tidak perlu initiative untuk percakapan. Dodge, Dash, atau meminta pertolongan lebih masuk akal.

## Mulai / Akhiri Fight

1. Pastikan ancaman atau tindakan nyata. Check sosial gagal atau menolak berbagi catatan bukan trigger initiative.
2. Jelaskan target, jarak, cover, dan posisi barang. Pembawa K-17 tidak otomatis menjatuhkannya saat diserang.
3. Terima tawaran ceasefire ketika situasi berubah; initiative tidak menutup percakapan.
4. Saat crew mundur atau alat berhenti, hentikan tekanan itu; tidak perlu menghabiskan HP.
5. Melumpuhkan tanpa membunuh mengikuti aturan melee/knockout 2024 meja. Ranged attack tidak dijamin nonlethal.
6. Catat cedera/kerusakan nyata. Tidak ada uang, loot, atau Resonansi otomatis dari mengalahkan crew/alat.

## CritterDB / Avrae

Bestiary JSON: **Assets/Mission G/Avrae/Mission G - CritterDB Bestiary.json**. Import sebagai **CritterDB Bestiary**, publish, lalu masukkan URL bestiary ke Avrae. Field **CR 0 / XP 0** adalah placeholder, bukan perhitungan keseimbangan.

Serangan biasa dikenali sebagai attack roll dan damage. **Fall Back, Hold Position, Handling Circuit, dan Shutdown Latch diselesaikan manual**, termasuk durasi, movement, save, dan limited uses. Tidak ada auto-damage tanpa save pada Hold Position.

Preset encounter mengatur jumlah/HP sesuai tabel. HP override tidak mengubah ability scores atau hit dice dasar. Jangan memakai roll HP jika ingin nilai tabel tetap. Lihat [[Mission G - VTT Preparation]] untuk command.

