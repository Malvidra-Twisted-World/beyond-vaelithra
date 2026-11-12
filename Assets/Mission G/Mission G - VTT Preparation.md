---
tags: [DnD, Mission, VTT, Avrae, DM Only]
mission: G
status: Local asset prep; see validation report for current checks
visibility: DM Only
---

# Mission G — VTT & Avrae Preparation

[[Mission G Overview]] · [[Mission G Script]] · [[Mission G - Combat Preparation]] · [[Mission G - Handouts]]

> [!info] Grid source
> **1536 × 1024 px · 24 × 16 square cells · 64 px per cell · 5 ft per cell.**  
> Offset awal X=0, Y=0. Jangan resize file saat upload. Tekstur ubin bukan grid arsitektur presisi. Jalur yang narasi nyatakan terbuka tetap terbuka jika dekorasi gambar bersinggungan dengan snap. Semua map player-safe tanpa label; key DM di bawah.
>
> Saat sumber diubah ukurannya, hitung grid baru = 64 × (lebar baru / 1536). Zoom layar tidak mengubah grid sumber.

## Paket & entry points

- **Assets/Mission G/mission-g-session-pack-v1.zip** — script, overview, prep, map, token, handout, CritterDB, alias, dan prompt produksi.
- **Assets/Mission G/mission-g-player-assets-v1.zip** — map/token/handout saja; jangan otomatis membagikan semua handout sebelum ditemukan.
- **Assets/Mission G/DM Map Guide.html** — pilih scene dan tampilkan/sembunyikan key posisi untuk persiapan DM. Jangan share versi DM ber-key ke pemain.
- **Assets/Mission G/Avrae/Mission G - CritterDB Bestiary.json** — empat profil Inggris.
- **Assets/Mission G/Avrae/Map Templates/** — tiga file install alias dan daftar uvar.

Wulan memakai token yang sudah dimiliki DM, tidak dibuat ulang. Token PC dari roster masing-masing. Tidak ada token naga karena naga tidak hadir dalam paket Tier I ini.

## Discord — setup sekali

1. Import JSON ke CritterDB: buat bestiary, **Import Creatures → CritterDB Bestiary**, paste seluruh teks JSON, import, publish.
2. Import URL bestiary ke Avrae, bukan URL JSON/Drive.
3. Buka masing-masing file install **mgscene**, **mgcrew**, **mgsentinel** di folder Map Templates. Salin seluruh isi satu file sebagai satu pesan. Masing-masing di bawah 2.000 karakter.
4. Simpan uvar berikut bila ingin mudah mengganti background. Alias terbaru juga memiliki URL default GitHub yang sama. Uvar lama selalu mengalahkan default.
5. Alias memakai prefix **!**. Jika prefix server berbeda, ganti juga prefix pada command di dalam file install.

```text
!bestiary import URL_BESTIARY_CRITTERDB
```

### G1 — Utility Cut

```text
!uvar mg_map_g1 https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/Assets/Mission%20G/Maps/G1-Utility-Cut.png
```

### G2 — Receiving Hall

```text
!uvar mg_map_g2 https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/Assets/Mission%20G/Maps/G2-Receiving-Hall.png
```

### G3 — Archive and Packing Floor

```text
!uvar mg_map_g3 https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/Assets/Mission%20G/Maps/G3-Archive-Packing.png
```

### G4 — Dispatch Bay

```text
!uvar mg_map_g4 https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/Assets/Mission%20G/Maps/G4-Dispatch-Bay.png
```

**Satu blok = satu pesan Discord.** URL harus publik dan menghasilkan gambar langsung. Link halaman preview/Drive bukan pengganti raw image URL. URL default mengikuti path repo GitHub. Tes tampilan dilakukan nanti melalui !map di Discord; tidak perlu tes render terpisah untuk menyelesaikan prep.

## Saat sesi — load scene

Mulai initiative sekali di channel khusus G bila belum aktif:

```text
!init begin
```

```text
!mgscene g1
```

```text
!map
```

Berikutnya pakai **!mgscene g2**, **g3**, atau **g4**, lalu **!map**. Jangan menjalankan !init end untuk mengganti map. Alias membuat combatant **DM** sebagai penampung map bila belum ada; nama DM jangan dipakai untuk NPC.

**Pindah scene mengganti background saja.** HP, initiative, note dan posisi token tidak direset. Setelah berpindah, tempatkan ulang sesuai perpindahan nyata. Angka koordinat yang sama pada scene baru tidak membuktikan karakter berpindah lokasi otomatis.

Player masuk via **!init join** memakai sheet mereka. Usulan slot masuk G3: L14, M14, L15, M15, K14; G4: L14, M14, K14, N14, L13. Sesuaikan urutan jalan dan tembok yang benar-benar terlihat.

```text
!map -t "NAMA_PC" -move L14
```

## Preset roster G4

Command menerima **jumlah PC 2 / 3 / 4 / 5**; default 4 jika diabaikan. Untuk party terkuras, gunakan baseline 2 PC atau kurangi tekanan secara manual. Roster bukan hitungan CR teruji.

**Crew, saat Ratri memang muncul:**

```text
!mgcrew 4
```

```text
!map
```

Ini menambah RS dan RH1. Untuk 5 PC, tambah RH2; untuk 2 PC, hanya RS dengan HP 18. Ratri yang sedang berbicara tidak otomatis menjadi penyerang.

**Sentinel, hanya setelah handling sengaja diaktifkan:**

```text
!mgsentinel 4
```

```text
!map
```

Ini menambah PS1–PS2 HP 16. Pada 2 PC, satu unit HP 14; pada 3 PC satu unit HP 22; pada 5 PC dua unit HP 22. Jangan memuat preset sentinel hanya untuk memberi ambience pada alat dorman.

Command roster melewati nama yang sudah ada, sehingga pengulangan setelah selesai tidak menyembuhkan atau memindahkan NPC lama. Mengganti parameter jumlah PC **tidak** mengubah HP NPC yang sudah ada atau menghapus unit berlebih. Tunggu command selesai sebelum mengulang; tidak ada lock untuk dua command bersamaan. Jangan memuat crew dan sentinel sebagai dua roster penyerang sekaligus.

Movement dan ability khusus tetap manual. Ranged serangan biasa punya attack roll/damage; Hold Position, Fall Back, dan shutdown tidak otomatis diterapkan oleh teks statblock.

## Scene & DM key

Semua titik tabel menunjuk **pusat cell**, bukan tembok presisi. Rumus pusat: X = (kolom−0,5)×64, Y = (baris−0,5)×64. Koordinat mulai A1 di kiri atas. Penempatan/arsitektur adalah staging usulan, bukan canon yang sudah dimainkan.

### G1 — Utility Cut

![](Assets/Mission%20G/Maps/G1-Utility-Cut.png)

| Key | Cell | Pusat px | Penggunaan |
|---|---|---|---|
| G1-A entry | M15 | 800, 928 | Datang dari jalan utilitas |
| Ramp kiri | G5 | 416, 288 | Pendekatan kering |
| Jalur kanan | S5 | 1184, 288 | Maintenance path |
| Threshold utara | L2 | 736, 96 | Pintu menuju G2; gambar menunjukkan bukaan, status tertutup/tidak terkunci disampaikan DM |
| Guard shack | U8 | 1312, 480 | Dressing/cover; tidak otomatis punya clue |

G1 dipakai kembali saat pulang lewat G2. Tidak ada musuh default atau hazard yang memblokir kedua rute. Koreksi gambar dipilih untuk top-down; varian awal perspektif disimpan hanya sebagai arsip produksi.

### G2 — Receiving Hall

![](Assets/Mission%20G/Maps/G2-Receiving-Hall.png)

| Key | Cell | Pusat px | Penggunaan |
|---|---|---|---|
| Entry | L15 | 736, 928 | Dari G1 |
| G2-A receiving desk | C8 | 160, 480 | Laci slip packing; ambil dari sisi meja yang bisa dijangkau |
| G2-B handling panel | W7 | 1440, 416 | OFF/ON hanya untuk G4; bukan kunci G3 |
| G2-C inspection bay | U13 | 1312, 800 | Tali/jejak pengunjung baru |
| Exit utara | L2 | 736, 96 | Ke G3 |

Chalk bay kecil adalah penanda kerja, bukan ritual utama. Pintu terbuka/tertutup ditentukan narasi tanpa memerlukan varian gambar.

### G3 — Archive and Packing Floor

![](Assets/Mission%20G/Maps/G3-Archive-Packing.png)

| Key | Cell | Pusat px | Penggunaan |
|---|---|---|---|
| Entry | L15 | 736, 928 | Dari G2 |
| G3-A upper desk | G7 | 416, 416 | Dokumen penelitian |
| G3-A lower desk | G11 | 416, 672 | Sketsa rute; boleh ditemukan di salah satu meja |
| G3-B cleared ritual | S9 | 1184, 544 | Sambungan dilepas; bukan portal/trigger |
| G3-C K-17 shelf | V4 | 1376, 224 | Kotak kecil pada rak alcove; **objek**, bukan NPC |
| Exit utara | L2 | 736, 96 | Ke G4 |

Ruang kiri/kanan berbagi aisle terbuka. K-17 adalah properti kecil; gunakan narasi atau marker objek, jangan mengubahnya menjadi creature hidup. Tidak ada identitas pemilik atau isi kotak yang terbaca dari map.

### G4 — Dispatch Bay

![](Assets/Mission%20G/Maps/G4-Dispatch-Bay.png)

| Key/token | Cell | Pusat px | Penggunaan |
|---|---|---|---|
| Entry | L14 | 736, 864 | Dari G3 |
| Exit | L2 | 736, 96 | Ramp ke luar; boleh kembali ke G1 |
| Trolley | L8–N10 | sekitar 800, 544 | Cover/obstacle; bukan monster |
| RS | H7 | 480, 416 | Ratri ketika dinarasikan |
| RH1 | R7 | 1120, 416 | Helper 1 |
| RH2 | H11 | 480, 672 | Helper 2 hanya jika dipakai |
| PS1 | H10 | 480, 608 | Sentinel kiri, baru aktif jika dipicu |
| PS2 | R10 | 1120, 608 | Sentinel kanan, bila roster memuat dua |
| Local latch approach | G10 / S10 | 416,608 / 1184,608 | Dekati unit 5 ft lalu gunakan prosedur shutdown |

Panel dalam gambar G4 boleh dijelaskan sebagai indikator/repeater; **OFF tanpa check pada script tetap panel G2**, agar tidak ada dua aturan berbeda. Latch selalu pada unit. Sentinel tidak menembus trolley atau mengejar keluar ruangan.

## Token roster

| File | Pemakaian |
|---|---|
| Tokens/Damar-Seta.png | Klien; hadir di briefing/Signal saja |
| Tokens/Ratri-Sembada.png | Salvage lead RS |
| Tokens/Recovery-Hand.png | RH1/RH2; duplikasi profil generik yang sama |
| Tokens/Packing-Sentinel.png | PS1/PS2; satu cell per unit |
| Wulan | Gunakan aset milik DM; tidak termasuk paket |
| PC | Gunakan token karakter masing-masing |

Semua empat token baru berbentuk portrait lingkaran dengan alpha di luarnya. Ukuran file portrait tidak mengubah ukuran creature Medium satu cell. Token berwarna adalah fallback Avrae; hosting portrait/raw URL tidak otomatis mengatur token shortcode alias map.

## Verification boundary

Lihat **Assets/Mission G/Production/validation-report.md** untuk hasil pemeriksaan lokal. Tes tampilan OTFBM akan dilakukan melalui Discord sesuai arahan DM. Paket tidak diklaim playtested, CR-balanced, atau sudah diuji pada bot server pengguna. Skala 64 px adalah skala permainan terpilih, bukan ukuran lokasi canon.

Sumber teknis: [Avrae commands](https://avrae.io/commands/), [Aliasing API](https://avrae.readthedocs.io/en/stable/aliasing/api.html), [CritterDB schema](https://github.com/haswellr/CritterDB/blob/master/server/models/creature.js), dan format map/notes yang mengikuti [Corvux planner](https://www.corvux.me/Avrae_Combat_Planner/). Image dibuat dengan built-in imagegen; prompt ada di Production/Prompts.md.

