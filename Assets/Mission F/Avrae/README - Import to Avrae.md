# Mission F — CritterDB → Avrae

File: [[Mission F - CritterDB Bestiary.json]]. Sumber: [[Mission F - Combat Preparation]]. Semua statblock dan ability berbahasa Inggris.

File JSON ini untuk **diimpor ke CritterDB**, bukan dilampirkan langsung ke command Avrae. Google Drive boleh dipakai untuk menyimpan atau mengirim file. URL yang dimasukkan ke Avrae adalah URL bestiary CritterDB, bukan URL Drive.

## Import ke CritterDB

1. Buka [CritterDB](https://critterdb.com/) dan login.
2. Buat bestiary bernama **Beyond Vaelithra — Mission F**.
3. Di bestiary itu, buka **Import Creatures** dan pilih format **CritterDB Bestiary**. Nama tombol dapat berbeda mengikuti versi UI.
4. Buka `Mission F - CritterDB Bestiary.json` sebagai teks, salin **seluruh isi JSON**, lalu tempel ke kolom import. Pilih format bestiary, bukan single creature.
5. Import dan pastikan muncul lima creature: **Garran Vey**, **Mara Vell**, **Wizard Associate**, **Unstable Echo**, dan **Surveyor**.
6. Gunakan fitur **Publish** bestiary, lalu salin URL bestiary yang dipublikasikan. Publishing membuat statblock dapat dilihat publik; tidak perlu memasukkan catatan rahasia cerita. File ini tidak menyertakan script atau panduan plot DM.

## Import ke Avrae

Jalankan dengan prefix server yang sesuai; contoh di sini memakai default `!`.

```text
!bestiary import <URL_BESTIARY_CRITTERDB>
!bestiary list
```

Ganti placeholder URL, termasuk tanda `< >`, dengan link sebenarnya. Jika perlu memilih ulang bestiary aktif:

```text
!bestiary "Beyond Vaelithra — Mission F"
```

Sesudah mengedit bestiary, publish ulang perubahan bila diperlukan oleh CritterDB, kemudian pada bestiary aktif jalankan:

```text
!bestiary update
```

## Memasukkan creature ke initiative

Di channel combat:

```text
!init begin
!init madd "Garran Vey"
!init madd "Mara Vell"
!init madd "Wizard Associate"
```

Ini roster konflik wizard. Jangan otomatis menambahkan Echo ke encounter yang sama. Untuk alternatif Echo, tambahkan **Unstable Echo** sebanyak jumlah yang dipilih DM, biasanya tiga atau dua jika party terkuras. Untuk pekerja, gunakan **Surveyor** bagi setiap pekerja yang perlu dilacak; profilnya sama untuk Bram, Yara, dan Surveyor 03–06. Lihat `!help init madd` untuk opsi penamaan dan penambahan beberapa creature di versi bot servermu.

Saat turn creature aktif:

```text
!init attack list
!init attack "Arcane Bolt" -t "NAMA_TARGET"
```

Contoh Arcane Bolt dipakai pada turn Garran. Nama target harus sesuai nama combatant di initiative.

## Yang otomatis dan yang manual

| Bagian | Perilaku paket |
|---|---|
| AC, HP, ability scores, saves, skills, speed, immunities | Dipetakan ke field CritterDB yang dibaca Avrae |
| Arcane Bolt, Staff, Spark, Arcane Dart, Arc Discharge | Teks serangan dikenali parser Avrae sebagai attack roll dan damage |
| Binding Field | Teks tetap tersedia; DM menyelesaikan STR save DC 13, Speed 0, repeat save memakai Action, durasi, dan 2 penggunaan per encounter secara manual |
| Repelling Gesture | STR save DC 12, dorongan 5 ft., dan 2 penggunaan per encounter ditangani manual |
| Containment Ward | DM melacak reaction dan 2 penggunaan per encounter; roll `!roll 1d6+2`, lalu sesuaikan damage/HP agar pengurangan diterapkan satu kali |
| Flicker Burst | DEX save DC 12 per creature dalam radius 5 ft.; gagal menerima `1d6` force, sukses 0. Pilih target dan terapkan damage manual. Parser damage-only sengaja dinonaktifkan untuk ability ini agar tidak mengabaikan saving throw |
| Unstable Pattern | Arcana DC 12 dan dua sukses kumulatif per Echo ditangani manual |
| Surveyor | Death saves adalah house rule rescue; tidak diklaim otomatis melalui trait |

Tidak ada penggunaan per-encounter yang diganti menjadi per-day. Jangan memakai `!cast` untuk ability homebrew ini seolah-olah spell resmi. Untuk Staff Mara, damage minimum 0 tetap berlaku; periksa hasil roll jika modifier menghasilkan nilai negatif.

## Data teknis dan batas verifikasi

| Creature | AC | HP | Hit dice untuk import |
|---|---|---|---|
| Garran Vey | 13 | 44 | 8d6 + 16 |
| Mara Vell | 12 | 22 | 4d8 + 4 |
| Wizard Associate | 12 | 16 | 3d8 + 3 |
| Unstable Echo | 12 | 18 | 4d6 + 4 |
| Surveyor | 10 | 9 | 2d8 |

CritterDB dan parser Avrae menghitung HP dari jumlah hit dice, ukuran die, dan CON. Hit dice di atas adalah pilihan konversi agar **HP tetap persis sama** dengan Combat Preparation; terutama Garran memakai d6 meskipun Medium. Ini tidak menetapkan class level atau metode recovery NPC. Jangan memakai opsi roll HP jika ingin HP tetap mengikuti tabel.

CR dan XP belum dihitung di sumber. Field **CR 0 / XP 0** diperlukan sebagai placeholder data; jangan membacanya sebagai penilaian kesulitan atau dasar reward. Proficiency bonus semua profil adalah +2; save/skill yang tertulis disimpan sebagai bonus eksplisit. Medium Humanoid pada Surveyor adalah metadata token pekerja generik, bukan penetapan ancestry pekerja bernama.

Image URL dibiarkan kosong: file lokal atau link halaman Drive belum merupakan direct image URL untuk token. Statblock import tidak memasang map atau alias mapping Discord. Konfigurasi map mengikuti bot/alias yang dipakai server.

Pemeriksaan lokal: JSON dapat dibaca, lima profil tersedia, AC/HP sesuai sumber, keenam serangan dikenali oleh regex parser publik Avrae, dan Flicker Burst tidak berubah menjadi serangan damage tanpa save. **Belum diuji dengan import akun CritterDB atau command bot Discord langsung.**

Sumber format yang diperiksa:

- [CritterDB — importer bestiary JSON](https://github.com/haswellr/CritterDB/blob/master/server/public/js/controllers/importCreature.js)
- [CritterDB — creature schema](https://github.com/haswellr/CritterDB/blob/master/server/models/creature.js)
- [Avrae — CritterDB parser](https://github.com/avrae/avrae/blob/master/cogs5e/models/homebrew/bestiary.py)
- [Avrae — command reference](https://avrae.io/commands/)
