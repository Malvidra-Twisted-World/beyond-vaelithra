# Mission G — CritterDB & Avrae Import

Source of truth: [[Mission G - Combat Preparation]]. Navigation: [[Mission G - VTT Preparation]].

## Import sekali

1. Buka CritterDB dan buat bestiary **Beyond Vaelithra — Mission G**.
2. Pilih **Import Creatures → CritterDB Bestiary**.
3. Buka **Mission G - CritterDB Bestiary.json**, salin seluruh teks JSON dan paste. Ini import bestiary, bukan single creature.
4. Pastikan ada **Ratri Sembada**, **Recovery Hand**, **Packing Sentinel**, dan **Damar Seta**.
5. Publish bestiary dan salin URL hasil publish. JSON tidak memuat script, handout, isi kotak, atau jawaban misteri.
6. Jalankan:

```text
!bestiary import URL_BESTIARY_CRITTERDB
```

```text
!bestiary "Beyond Vaelithra — Mission G"
```

Jika bestiary berubah, publish perubahan bila diperlukan lalu gunakan **!bestiary update** pada bestiary aktif. Jangan memasukkan link Drive, URL file JSON GitHub, atau URL map ke command bestiary import.

## Install preset

Salin isi masing-masing file berikut sebagai satu pesan Discord:

- Map Templates/mgscene - install.txt
- Map Templates/mgcrew - install.txt
- Map Templates/mgsentinel - install.txt

Alias memakai prefix !. Jangan timpa alias pribadi dengan nama sama tanpa memeriksa !alias list. Alias melakukan setup melalui command bawaan; panggil **!map** sendiri sesudah setup untuk render.

Uvar F1–F4 memakai awalan **mf**, sedangkan G1–G4 memakai **mg** sehingga tidak bentrok. Combat di channel yang sama tetap memakai satu initiative; jalankan G pada channel/thread yang sesuai agar tidak mengganti map sesi F aktif.

## Angka dasar

| Creature | AC | HP | Dice |
|---|---|---|---|
| Ratri Sembada | 13 | 27 | 5d8 + 5 |
| Recovery Hand | 12 | 11 | 2d8 + 2 |
| Packing Sentinel | 13 | 22 | 4d8 + 4 |
| Damar Seta | 10 | 9 | 2d8 |

CR 0 / XP 0 pada data adalah **placeholder import**, bukan penilaian encounter atau reward. Semua PB +2, save/skill khusus disimpan sebagai bonus eksplisit. Hit dice menghasilkan HP dasar yang sama pada formula CritterDB dan parser Avrae.

Preset **mgcrew N** dan **mgsentinel N** memakai override jumlah/HP dari tabel scaling di Combat Preparation. Jangan memakai -rollhp bila ingin HP tabel tetap. Tidak ada reset HP saat alias diulang; nama yang sudah ada dilewati.

## Automation boundary

| Bagian | Implementasi |
|---|---|
| AC, HP, six ability scores, saves, skills, immunities | Field CritterDB |
| Survey Bolt, Light Baton, Baton, Hand Crossbow, Padded Clamp, Improvised Strike | Attack roll dan dice damage dari deskripsi Inggris |
| Fall Back | Reaction, trigger, gerak, Opportunity Attack exception dan 1/encounter ditangani DM |
| Hold Position | STR save DC 12, Speed 0, durasi dan 2/encounter ditangani DM |
| Handling Circuit / Shutdown Latch | Dormansi, check/Action, dan akhir efek ditangani DM |
| Morale | Keputusan NPC dan ceasefire; bukan auto-win mechanic |

Portrait URL mengarah ke raw PNG GitHub. Alias map tetap memakai marker warna; image pada monster tidak menjamin shortcode map langsung terpasang. VTT biasa dapat memakai file token PNG.

**Verifikasi:** lihat ../Production/validation-report.md. Pemeriksaan lokal bukan import melalui akun CritterDB atau eksekusi bot Discord. Profil homebrew belum playtested.

Sumber: [CritterDB schema](https://github.com/haswellr/CritterDB/blob/master/server/models/creature.js), [Avrae CritterDB parser](https://github.com/avrae/avrae/blob/master/cogs5e/models/homebrew/bestiary.py), [Avrae commands](https://avrae.io/commands/).

