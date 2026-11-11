	# Mission F — Map & Encounter Presets for Avrae

[[Mission F - VTT Preparation]] · [[Mission F - Combat Preparation]] · [[README - Import to Avrae]]

Template ini disiapkan untuk **alias `!map` berbasis OTFBM** dengan format notes `Location / Size / Color` dan effect `map`. Pengguna sudah mengonfirmasi command `!map`; versi atau link Workshop alias server belum diperiksa. Jika `!map` servermu merupakan implementasi lain, gunakan fallback command di bawah dan cocokkan `!map help`.

## Setup sekali sebelum sesi

### 1. Import bestiary

Ikuti [[README - Import to Avrae]]. Bestiary harus aktif untuk akun DM sebelum memakai preset roster. Creature yang dicari template: Garran Vey, Mara Vell, Wizard Associate, Unstable Echo, Surveyor.

### 2. Konfigurasi URL gambar map

Keempat map memakai direct image URL dari repo publik **Malvidra-Twisted-World/beyond-vaelithra**, branch **master**. Alias terbaru sudah menyertakan default URL F1–F4; tidak perlu hosting terpisah.

Jika alias versi lama sudah dipasang, atau user variable sebelumnya masih menunjuk Imgur, jalankan satu per satu:

```text
!uvar mf_map_f1 https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/Assets/Mission%20F/Maps/F1-Approach-Route.png
!uvar mf_map_f2 https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/Assets/Mission%20F/Maps/F2-Outer-Facility.png
!uvar mf_map_f3 https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/Assets/Mission%20F/Maps/F3-Service-Tunnel.png
!uvar mf_map_f4 https://raw.githubusercontent.com/Malvidra-Twisted-World/beyond-vaelithra/master/Assets/Mission%20F/Maps/F4-Sublevel-2.png
```

User variable mengalahkan URL default alias. Karena itu, update variable F3 di atas jika sebelumnya memakai Imgur.

Semua gambar asli berukuran **1536 × 1024 px**. Grid **24 × 16**, **64 px per kotak**, **5 ft per kotak**. URL GitHub harus melayani gambar publik tanpa login. Link `github.com/.../blob/...` adalah halaman preview; preset menggunakan `raw.githubusercontent.com`.

### 3. Install empat alias pribadi

Buka file `.txt` berikut, salin seluruh isi, dan kirim **masing-masing sebagai satu pesan tersendiri** ke Discord. Setiap pesan sudah menyertakan `!alias` dan berukuran di bawah 2.000 karakter.

- `mfscene - install.txt` — simpan/pilih background F1–F4.
- `mfwizards - install.txt` — Garran, Mara, satu Wizard Associate.
- `mfrescue - install.txt` — keenam pekerja.
- `mfecho - install.txt` — dua atau tiga Echo opsional.

Nama alias ini memakai awalan `mf`; cek `!alias list` sebelum instalasi jika sebelumnya kamu sudah punya alias dengan nama yang sama. Template memakai prefix default `!`; ubah prefix pada command di dalam file jika server memakai prefix lain. Jangan mengirim file sebagai attachment dan berharap bot mengeksekusinya: yang dikirim adalah teks isinya.

Alias menggunakan command bawaan Avrae untuk setup. Alias tidak memanggil `!map` dari dalam alias lain, karena Avrae melarang alias memanggil alias. Setelah setup, jalankan `!map` sendiri untuk merender.

## Saat sesi: load scene

Mulai initiative sekali di channel sesi:

```text
!init begin
```

Pilih scene dan tampilkan map:

```text
!mfscene f1
!map
```

Pindah scene dengan cara yang sama:

```text
!mfscene f2
!map
```

`!mfscene f3` untuk Service Tunnel; `!mfscene f4` untuk Sublevel 2. Command membuat combatant penampung map bernama **DM** jika belum ada, lalu mengganti effect **map** pada combatant itu. Biarkan DM sebagai penampung map tanpa peran combat. Jangan gunakan nama DM untuk NPC lain.

**Pindah scene hanya mengganti map. HP, initiative, notes, dan posisi token combatant lain tidak direset.** Karena koordinat berada pada sistem gambar yang sama, setelah pindah lokasi sesuaikan posisi token yang terlihat; jangan menganggap NPC otomatis berpindah tempat secara naratif. F1/F2/F4 tidak menambahkan musuh atau encounter baru.

### F3 — rescue dan negosiasi

```text
!mfscene f3
!mfrescue
!map
```

Player masuk ke initiative melalui `!init join` memakai sheet aktif masing-masing. Posisi awal PC adalah pilihan meja. Usulan titik masuk F3: D12, E12, F12, D13, E13; gunakan nama combatant sebenarnya saat menempatkan token.

Contoh:

```text
!map -t "NAMA_PC" -move D13
```

### Wizard muncul / konflik dimulai

```text
!mfwizards
!map
```

Ini menambahkan **GV**, **MV**, **WZ**. Panggil saat mereka benar-benar perlu ditampilkan; jangan memuatnya di awal kalau ingin menjaga kemunculan Garran. Penambahan ke initiative tidak otomatis berarti NPC menyerang. Negosiasi tetap dapat menyelesaikan encounter.

### Alternatif Echo

Gunakan hanya jika opsi monster dipilih DM:

```text
!mfecho 3
!map
```

Atau `!mfecho 2` jika party terkuras. Command menambahkan E1–E3 atau E1–E2 dengan marker Small. Ini bukan tambahan wajib untuk konflik wizard.

**Preset roster melewati combatant yang namanya sudah ada.** Menjalankannya ulang setelah selesai tidak menyembuhkan NPC, tidak memindahkan NPC lama kembali, dan tidak menambah duplikat nama yang sama. Tunggu satu command selesai sebelum mengulang; pemeriksaan ini bukan penguncian untuk dua command yang dikirim bersamaan. `!mfecho 2` tidak menghapus E3 yang sudah ada; jumlah itu hanya membatasi penambahan.

## Penempatan F3

Koordinat memakai A1 di kiri atas, A–X untuk kolom dan 1–16 untuk baris. Posisi disarankan untuk staging, bukan actual-play canon. Sebagian posisi pekerja dari DM key digeser ke row 6 setelah gambar diperiksa agar pusat token tidak jatuh di tembok selatan refuge. Prioritaskan jalur yang dapat dilalui jika dekorasi gambar bersinggungan dengan grid.

| Nama initiative | Profil | Koordinat | Marker |
|---|---|---|---|
| GV | Garran Vey | L9 | Purple |
| MV | Mara Vell | M6 | Blue |
| WZ | Wizard Associate | S9 | Green |
| Bram | Surveyor | P6 | Orange |
| Yara | Surveyor | R6 | Yellow |
| S03 | Surveyor | T6 | Blue |
| S04 | Surveyor | V6 | Green |
| S05 | Surveyor | U4 | Red |
| S06 | Surveyor | U3 | Purple |
| E1 | Unstable Echo | J9 | Cyan |
| E2 | Unstable Echo | N9 | Cyan |
| E3 | Unstable Echo | Q9 | Cyan |

Wizard dan Echo sengaja ditaruh di corridor yang sama karena merupakan dua pilihan tekanan encounter. Jangan otomatis memakai kedua roster sebagai penyerang sekaligus. Pekerja tidak otomatis mengikuti PC saat bergerak.

## Menjalankan battle

```text
!init next
!init attack list
!init attack "Arcane Bolt" -t "NAMA_TARGET"
```

Contoh serangan dipakai saat turn GV. Pemindahan manual token:

```text
!map -t GV -move M9
```

Template memakai marker warna agar tidak bergantung pada hosting portrait token. Map bukan sistem collision, fog dinamis, atau pengukur line of sight otomatis. Pergerakan, cover, dan penentuan target tetap mengikuti keputusan DM. Lihat [[README - Import to Avrae]] untuk ability yang perlu diselesaikan manual.

## Kalau background tidak muncul

Coba di channel percobaan terlebih dahulu:

```text
!init begin
!init add 0 DM -p 20
!map -t DM -mapsize 24x16 -options c64 -bg "URL_PUBLIK_F3"
```

Jika initiative atau DM sudah ada, lewati dua command pertama. Ganti URL dengan gambar sebenarnya. Jika cara langsung ini bekerja tetapi `!mfscene f3` tidak, kemungkinan versi alias menyimpan konfigurasi map dengan cara lain; template belum cocok dengan versi server itu. Jangan menghapus combat sesi untuk mengetesnya.

Jika background tidak tampil dengan kedua cara, cek akses URL, format PNG/JPEG, serta respons layanan OTFBM. Endpoint OTFBM tidak berhasil diperiksa melalui web fetch dalam proses pembuatan paket, sehingga keberhasilan render belum dikonfirmasi. Isi `mf_map_f3` dapat diperiksa dengan `!uvar mf_map_f3`. Pengujian sebelumnya menghasilkan HTTP 200 tanpa background dan dengan background GitHub pembanding, tetapi HTTP 502 dengan URL Imgur F3; ukuran grid yang sama berhasil pada kedua kontrol.

## Batas verifikasi

File alias diperiksa secara lokal untuk logika pemilihan scene, validasi URL kosong, penggantian effect map, pencegahan duplikat roster secara berurutan, dan opsi 2/3 Echo menggunakan mock API yang mengikuti dokumentasi. Pemeriksaan ini **bukan eksekusi Draconic/Avrae langsung**. Keempat URL GitHub sudah dikonfigurasi. Verifikasi akses publik dan render F3 dicatat terpisah setelah push; uji bot Discord pada server pengguna belum dilakukan. F3 diperiksa secara visual; F1/F2/F4 memakai metadata ukuran paket yang sudah ada.

Sumber:

- [Avrae — commands dan multiline](https://avrae.io/commands/)
- [Avrae — aliasing API](https://avrae.readthedocs.io/en/stable/aliasing/api.html)
- [Avrae — alias tidak dapat memanggil alias](https://avrae.readthedocs.io/en/stable/aliasing/aliasing.html)
- [Corvux — Avrae/OTFBM Combat Planner](https://www.corvux.me/Avrae_Combat_Planner/): format effect map, notes posisi, dan opsi grid mengikuti command generator ini; alias `!map` server belum diinspeksi.
