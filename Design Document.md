# Beyond Vaelithra: Design Document

> **Status:** Draft v0.2 — fondasi sistem, belum ada starter mission.
> **Terkait:** [[Factions]] · [[Districts]] · [[Dashboard]]

Dokumen ini adalah fondasi desain untuk **Kartaloka West Marches**, sebuah PbP Discord campaign berformat sandbox di kota **Kartaloka**, sebuah kota di realm Dewanegara. Ini bukan naskah cerita — ini adalah *struktur permainan*. Lore ditulis seminimal mungkin, cukup untuk memberi rasa dan pijakan.

> **Konvensi penamaan:** semua proper noun desain (hub, district, faction, sistem) pakai Inggris. Deskripsi dan prosa tetap Indonesia.

---

## 1. Core Concept

### 1.1 Setting Pitch

**Kartaloka** — kota pelabuhan-industri terbesar di Dewanegara, berdiri beberapa abad setelah [[../../Worlbuilding/Story/Locations/Dewanegara|The Sundering War]]. Era ini disebut warga lokal **Age of Restoration**: setelah abad-abad pertumbuhan pasca-perang, Dewanegara mengalami sesuatu yang setara revolusi industri — tapi magic ikut berkembang bersamanya, bukan digantikan olehnya.

Rasanya seperti *Watch Dogs (2014)*, bukan cyberpunk:

| Ada | Tidak ada |
|---|---|
| Smartphone, internet, medsos | Neon everywhere, hologram, flying car |
| CCTV + *ward-grid* magis berdampingan | Dystopia korporat sebagai default |
| Bank, ATM, minimarket, apartemen, commuter rail | Teknologi jauh melampaui hari ini |
| Kepolisian modern + divisi kejahatan magis | Magic sebagai "gimmick" dekoratif |
| Corporate culture, sindikat kriminal terorganisir | Fantasy race/monster sebagai hal aneh |

Prinsip pegangan: **magic adalah satu layer tambahan dalam masyarakat, bukan pengganti teknologi.** Kalau sebuah adegan bisa terjadi di kota modern kita hari ini dengan sedikit twist gaib, itu levelnya sudah pas. Kalau adegan butuh hologram atau kendaraan terbang untuk masuk akal, itu sudah kelewat jauh — mundurkan.

### 1.2 Kenapa Kartaloka, bukan Vaelithra?

Dewanegara di lore lama (Dewanginokori, Silver Light, kemunculan Vaelithra) berlangsung **beberapa abad lebih awal**, di fase awal pasca-perang. Kartaloka berdiri jauh di kemudian hari, di wilayah dan garis waktu yang **belum pernah disentuh Saga utama**. Artinya:

- Kamu boleh main puluhan mission di sini tanpa Vaelithra, Vaeil, atau Silver Light disebut sama sekali.
- Kalau sebuah thread butuh koneksi ke cosmology besar (misalnya lewat [[Factions#The Night Remnant|The Night Remnant]], lihat [[Districts#The Fringe|The Fringe]]), itu opsional dan harus muncul organik dari konsekuensi pemain — bukan dipaksakan dari awal.
- Silver Light, kalau disebut sama sekali, di era ini sudah menjadi institusi keagamaan mapan yang biasa saja — bukan plot device otomatis.

### 1.3 Magic-Tech Layering — Contoh Konkret

Supaya konsisten lintas DM, pakai pola ini tiap kali membuat institusi baru:

- **Signal** — aplikasi smartphone standar kota (chat, peta, pembayaran). Beberapa punya *ward-encryption* opsional (add-on legal dari [[Factions#The Script Order|The Script Order]]) untuk komunikasi yang tak bisa disadap scrying maupun hacking biasa.
- **Kepolisian** — detektif biasa untuk kasus biasa; **Scale Division** (lihat [[Factions]]) dipanggil kalau ada indikasi sihir/makhluk gaib.
- **Rumah sakit** — dokter dan cleric bekerja di ruangan yang sama; rekam medis mencatat status "arcane exposure" seperti mencatat alergi.
- **Keamanan gedung** — CCTV, keycard, DAN warding rune di pintu darurat. Satpam manusia + *construct* penjaga kecil untuk gedung premium.
- **Transportasi umum** — commuter rail biasa, tapi rel di beberapa distrik dilindungi ward anti-hantu peninggalan perang (karena beberapa terowongan tua dibangun di atas medan perang lama).

> **Catatan DM:** kalau ragu apakah sebuah ide "kelewat cyberpunk" atau "kelewat generik-fantasy", uji dengan pertanyaan: *apakah ini bisa dijelaskan sebagai versi modern dari sesuatu yang sudah ada di dunia nyata, ditambah satu twist magis?* Kalau ya, cocok.

---

## 2. Format Permainan

**West Marches-inspired, bukan West Marches literal.** Perbedaan paling penting dari West Marches klasik: campaign ini **tidak pakai leveling bebas per individu**. Alasannya murni praktis — di PbP async, rate aktivitas tiap pemain jomplang jauh, dan kalau leveling dibiarkan organik per-mission-per-orang, dalam sebulan bisa ada karakter level 8 duduk semeja sama karakter level 2 di mission yang sama. Itu tidak playable. Jadi struktur levelnya **tier-gated** (detail §2.2), sisanya tetap West Marches: pool pemain terbuka, party dibentuk per-mission, async, dunia persisten.

Aturan main:

- Tidak ada kewajiban posting harian. Scene boleh berhenti kalau satu pemain offline, lanjut kapan saja mereka kembali (soft-pause, bukan dianggap absen/DNF).
- Party dibentuk per-mission dari pool pemain yang available, **dalam Party Tier yang sama** (lihat §2.2) — bukan fixed party, tapi bukan sembarang gabung juga.
- Beberapa mission berjalan **paralel** di channel/thread berbeda, termasuk paralel lintas-tier (party Tier I dan Tier II bisa jalan bersamaan di distrik yang sama, mengerjakan hal berbeda).
- Dunia **persisten**: hasil satu mission memengaruhi mission lain, bahkan yang dimainkan party berbeda.
- Sesi tidak "reset". Kalau sebuah quest gagal, gagalnya permanen sampai ada pihak yang memperbaikinya lewat mission baru.

### 2.2 Party Tier — Sistem Level Tetap per Mission

Setiap mission punya **Party Tier** yang mengunci level karakter yang boleh ikut — mirip struktur organized play (Adventurers League), bukan level-agnostic sandbox murni.

| Tier | Level Karakter | Rasa Cerita |
|---|---|---|
| **Tier I** | 1–4 | Job jalanan, kejahatan lokal, kasus kecil |
| **Tier II** | 5–10 | Faction-level, mulai ada supernatural signifikan |
| **Tier III** | 11–16 | District-level crisis, lawan terorganisir besar |
| **Tier IV** | 17–20 | City-wide/cosmic stake, sisa peninggalan Sundering War |

**Aturan:**
- Karakter naik level lewat **milestone** yang ditetapkan per mission/arc yang selesai (bukan XP tracking manual) — tapi milestone **tidak akan pernah mendorong karakter melewati batas atas tier-nya**. Karakter mentok di level 4 tetap di Tier I sampai ikut *Tier Transition mission* (lihat di bawah).
- **Tier Transition Mission** — mission capstone khusus (ditandai jelas di board) yang jadi syarat naik ke tier berikutnya. Selesai capstone Tier I → karakter boleh ambil job Tier II dan levelnya otomatis naik ke ambang bawah tier baru (level 5). Ini mencegah gap individual yang liar sekaligus memberi rasa "naik kelas" yang jelas.
- Party campuran tier **tidak diizinkan** ikut mission yang sama — ini hard rule, bukan saran, karena tanpa ini seluruh alasan sistem tier runtuh.
- Karakter baru selalu masuk di Tier terendah yang masih terbuka untuknya (biasanya Tier I, kecuali pemain lama membuat karakter baru dan DM approve entry point lebih tinggi berdasar alasan naratif).

Field **Party Tier** ini ditambahkan ke Mission Card (lihat §5.2) sebagai hard requirement, terpisah dari **Trust Tier** (§4.4) yang mengatur akses berbasis reputasi terhadap faction, bukan level.

### 2.3 Masalah Praktis yang Perlu Diantisipasi (dan solusinya)

⚠️ **Kritik desain:** format ini punya risiko nyata kalau tidak dipagari sejak awal:

| Risiko | Kenapa berbahaya di async PbP | Mitigasi |
|---|---|---|
| **Party mismatch** — satu pemain jauh lebih maju/kuat dari yang lain | Rate aktivitas online tiap pemain beda jauh | Diselesaikan struktural lewat **Party Tier** (§2.2) — bukan mitigasi tambahan, tapi desain intinya |
| **Dua party menyelesaikan mission yang saling kontradiktif** (Party A menyelamatkan NPC, Party B — di thread lain — membunuhnya) | Karena berjalan paralel & async, ini bisa benar-benar terjadi | Terapkan **Canon Lock**: begitu satu thread mission resmi ditutup (bukan draft), DM utama mengunci outcome-nya di [[Dashboard]] dalam 24 jam. Mission lain yang overlap otomatis disesuaikan naratif ("kalian dengar kabar itu sudah terjadi") |
| **Scene macet** karena satu pemain hilang tanpa kabar | Async artinya tidak ada jaminan siapa online kapan | Beri tiap mission thread status jelas: `Active / Paused / Stale`. Thread `Stale` >14 hari boleh di-*soft-resolve* DM dengan hasil netral supaya tidak mengganjal world state |
| **DM burnout** karena harus jaga banyak thread + world state sekaligus | Ambisi "dunia hidup" gampang jadi beban admin | Lihat §6 World State System — sistemnya sengaja dibuat ringan, bukan simulasi penuh |

---

## 3. The Hub — The Switchboard

### 3.1 Konsep

**The Switchboard** — bukan tavern. Ia adalah *fixer exchange* yang menempati **Westa Tower**, bekas menara radio siaran kota dari awal era industrialisasi Kartaloka, di [[Districts#Old Town|Old Town]]. Menara ini berhenti siaran puluhan tahun lalu setelah stasiun radio bangkrut, lalu diambil alih dan direnovasi jadi ruang campuran: co-working space, kedai kopi, dan brokerage informasi/kontrak — dengan basement berisi *dead-drop locker* bagi klien yang tidak mau bertatap muka.

Nama "The Switchboard" sengaja dipilih sebagai metafora langsung: dulu menara ini menyambungkan sinyal radio ke seluruh kota, sekarang ia menyambungkan **klien ke fixer** — operator manual di tengah, bukan sistem otomatis.

**Kenapa fixer datang ke sini:** The Switchboard adalah satu-satunya tempat di kota yang **netral** — tidak dikuasai polisi, korporat, sindikat, atau ordo sihir manapun. Statusnya dijamin oleh kesepakatan tak tertulis lintas faksi (lihat [[Factions]]): siapa pun yang macam-macam di dalam Switchboard akan di-blacklist oleh semua faksi sekaligus. Ini membuat Switchboard jadi satu-satunya tempat aman untuk deal lintas-faksi.

### 3.2 Sejarah Singkat

Westa Tower dulunya stasiun radio "Radio Westa" yang menyiarkan berita dan drama radio kota selama puluhan tahun. Setelah bangkrut, gedung ini dibeli oleh **Wulan Kertadjaja**, mantan jurnalis investigasi yang di masa lalu terlibat kasus yang membuatnya "disumpah" oleh sebuah entitas kecil (detail sengaja tidak dijelaskan — bisa jadi hook) sehingga **ia secara harfiah tidak bisa berbohong demi keuntungan pribadi**. Kutukan/berkah ini justru jadi aset: semua pihak percaya Wulan tidak akan mengkhianati kesepakatan broker demi uang.

### 3.3 NPC Penting

- **Wulan Kertadjaja** — pengelola The Switchboard. Tenang, blak-blakan, dihormati semua faksi karena netralitasnya. Tidak ikut campur isi kontrak, hanya menjamin proses adil.
- **The Ledger** — bukan orang: sebuah *ledger* (buku besar) yang disemayamkan roh administratif tua peninggalan pra-perang, ditemukan Wulan di gudang menara. The Ledger mengelola **escrow pembayaran** dan **kontrak anonim** (lihat §4.3). Ia bicara lewat tulisan yang muncul sendiri di halamannya, gaya bahasanya formal dan sedikit sarkastik.
- **Reno "Kabel" Amran** — teknisi menara, mantan hacker independen, sekarang setengah legal menjaga sistem *Signal* Switchboard tetap tak terlacak. Sumber informasi teknis/digital. Dia juga yang secara teknis mem-publish **Signal Feed** (berita publik kota, lihat §3.4 & Discord Setup) — The Ledger yang "mendiktekan" isinya lewat tulisan yang muncul di halamannya, Reno yang mengetik ulang jadi post ke *Signal* karena The Ledger sendiri tidak punya cara langsung akses jaringan digital.
- **Ibu Tumini** — penjaga kedai kopi di lantai dasar. Tahu segalanya soal gosip jalanan biasa (bukan gosip faksi) karena semua orang lewat kedainya. RP hub paling santai.

### 3.4 Fasilitas

| Lantai | Fungsi |
|---|---|
| Basement | Dead-drop locker (kontrak anonim, barang bukti sensitif), ruang aman untuk klien yang tak mau dikenali |
| Lantai Dasar | Kedai kopi Ibu Tumini — ruang RP santai antar-pemain |
| Lantai 2 | Papan kontrak fisik + terminal digital tersambung ke **The Ledger** |
| Lantai 3 | Co-working space — meja kerja, rak referensi kota (peta, arsip berita lama) |
| Lantai Puncak (bekas ruang siaran) | Kantor Wulan, dipakai juga untuk negosiasi/pertemuan privat berisiko tinggi |

### 3.5 Bagaimana Pemain Berinteraksi dengan Hub

- **Cek papan kontrak** (fisik atau via app *Signal* — sinkron) untuk lihat mission tersedia, sudah difilter otomatis sesuai Party Tier karakter aktif pemain.
- **RP bebas** di kedai kopi — ini secara sengaja didesain jadi tempat party terbentuk secara organik ("eh, kamu juga ambil job Wavedock?").
- **Lapor hasil mission** ke Wulan atau langsung ke The Ledger untuk cairkan escrow — ini juga titik update [[Dashboard|World State]] oleh DM.
- **Titip rumor/informasi** ke Ibu Tumini atau Reno sebagai side-income kecil (bisa jadi mekanisme reward non-combat).

---

## 4. Fixer Network — Sistem Kontrak

### 4.1 Siapa Bisa Memasang Kontrak

Siapa saja — civilian, bisnis, korporat, pemerintah/polisi, peneliti, sesama adventurer, organisasi kriminal, klien anonim, bahkan entitas supernatural (lewat perantara, karena banyak dari mereka tak bisa masuk kota begitu saja). Setiap kontrak dicatat **The Ledger** dengan tag klien (lihat §4.4 Trust Tier).

### 4.2 Alur Kontrak

1. Klien mengajukan kontrak (datang langsung, lewat *Signal*, atau dead-drop anonim).
2. Wulan/The Ledger melakukan *sanity check* dasar (bukan penipuan jelas, bukan kontrak ilegal ekstrem seperti pembunuhan warga sipil polos — itu ditolak otomatis).
3. Kontrak naik ke papan dengan **Mission Card** (lihat §5.2), termasuk Party Tier yang sesuai tingkat bahaya.
4. Pemain klaim mission (siapa cepat, kecuali mission ber-*Trust Tier* tinggi).
5. Party menyelesaikan (atau tidak) → lapor ke Switchboard.
6. The Ledger mencairkan escrow, DM update world state.

### 4.3 Pembayaran & Escrow

Klien menitipkan bayaran ke **The Ledger** di muka (uang, barang, atau *favor* yang dicatat sebagai utang sosial). The Ledger menahan sampai:

- Fixer & klien sama-sama konfirmasi selesai, **atau**
- Fixer memberi bukti penyelesaian yang cukup meyakinkan Wulan (kalau klien menghilang/tak bisa dihubungi — sering terjadi di kontrak anonim).

Sengketa pembayaran diputuskan Wulan sebagai wasit netral — ini juga sumber RP/mission tersendiri ("klien menolak bayar, apa yang kalian lakukan?").

### 4.4 Reputasi — Trust Tier (bukan skor tunggal)

⚠️ **Kritik desain:** sistem reputasi numerik tunggal ("Reputation: 47/100") gampang jadi beban bookkeeping yang tidak ada yang benar-benar pakai di PbP santai. Jadi dipakai sistem **kualitatif per kelompok klien**, bukan satu angka global. **Trust Tier ini tidak ada hubungannya dengan Party Tier (§2.2)** — satu soal akses reputasi, satu lagi soal level karakter. Jangan disamakan.

| Tier | Makna | Akses |
|---|---|---|
| **Unknown** | Default semua fixer baru | Mission publik tier 1 saja |
| **Known** | Sudah beberapa kali kerja untuk kelompok ini | Mission tier 2, klien mulai sebut nama fixer di kontrak berikutnya |
| **Trusted** | Track record konsisten | Mission tier 3, akses kontrak semi-privat |
| **Inner Circle** | Klien ini menganggap fixer sekutu | Mission eksklusif, kadang diminta bantuan di luar kontrak formal (hook personal) |

Tier ini dilacak **per faksi/kelompok klien** (lihat [[Factions]]), bukan per karakter individu — jadi kalau satu party campuran mengerjakan job untuk polisi, semua fixer yang terlibat naik satu tingkat trust dengan **Scale Division**, bukan cuma satu karakter. Ini menghindari micromanagement per-PC yang berat untuk sistem async.

DM cukup mencatat ini di satu tabel sederhana di [[Dashboard]] — lihat §6.

### 4.5 Kontrak Anonim

Klien bisa minta identitasnya disembunyikan The Ledger. Konsekuensi mekanis:

- Payout biasanya **20-30% lebih tinggi** (kompensasi risiko tak tahu siapa/apa motif klien).
- Fixer tidak bisa naik Trust Tier dari kontrak ini (karena "klien"-nya secara resmi tidak diketahui) — **kecuali** mereka berhasil mengungkap identitas klien selama mission (jadi ini insentif eksplorasi, bukan cuma flavor).
- DM boleh sengaja bikin sebagian kontrak anonim berasal dari faksi yang sedang trust rendah dengan party, menyamar — ini legitimate source of "kontrak yang menjebak" tanpa railroad, karena pemain sendiri yang pilih ambil resiko anonim itu.

---

## 5. Mission Board

### 5.1 Kategori Mission

| Kategori              | Contoh Hook Singkat                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| Investigation         | "Ada pola pencurian aneh di gudang yang sama tiap bulan purnama."                                            |
| Missing Person        | "Anak kami tidak pulang dari Lantern District tiga hari lalu."                                               |
| Recovery              | "Ambil kembali barang pusaka keluarga dari rentenir."                                                        |
| Escort                | "Antar saksi ke pengadilan tanpa ketahuan siapa pun."                                                        |
| Extraction            | "Keluarkan informan kami dari dalam gudang Wave Family sebelum ketahuan."                                    |
| Surveillance          | "Awasi gerak-gerik pejabat ini selama seminggu, jangan sampai sadar."                                        |
| Bounty                | "Buronan kabur ke The Fringe, kami butuh dia hidup untuk ditanyai."                                          |
| Supernatural Activity | "CCTV toko kami rusak tiap malam Selasa, tak ada penjelasan teknis."                                         |
| Corporate Job         | "Audit keamanan gudang riset kami — diam-diam, jangan lewat jalur resmi."                                    |
| Criminal Job          | "Kami butuh sesuatu 'diamankan' dari kompetitor, tanpa kekerasan kalau bisa."                                |
| Police Request        | "Butuh konsultan independen untuk kasus yang bukan yurisdiksi biasa."                                        |
| Occult Investigation  | "Simbol ini muncul di lima TKP berbeda, kami tidak tahu artinya."                                            |
| Social/Negotiation    | "Mediasi sengketa lahan antara dua keluarga sebelum jadi kekerasan."                                         |
| Urban Exploration     | "Ada terowongan tua di bawah stasiun yang tak ada di peta resmi."                                            |
| Monster Hunting       | "Sesuatu memburu anjing liar di pinggir The Fringe, makin berani tiap minggu."                               |
| Mystery               | "Semua jam di satu blok apartemen berhenti di jam yang sama tiap hari."                                      |
| Heist                 | "Kami butuh dokumen ini keluar dari brankas sebelum rapat dewan Jumat."                                      |
| Protection            | "Saksi ini butuh pengawalan sampai sidang minggu depan."                                                     |
| Delivery              | "Paket ini tidak boleh lewat pemeriksaan resmi — jangan tanya kenapa."                                       |
| Faction-related       | "[[Factions#The Beacon Circle\|The Beacon Circle]] butuh bantuan menghadapi intimidasi dari preman bayaran." |

### 5.2 Mission Card — Template Praktis DM

Setiap mission dicatat DM dengan kartu ringkas ini (cukup di Obsidian, satu note per mission):

```
# [Judul Mission]
Kategori: 
Klien: (nama / "Anonim" via The Ledger)
Distrik: 
Party Tier: I / II / III / IV   (hard requirement level karakter)
Trust Tier dibutuhkan: 
Payout: 
Risk Level: Rendah / Sedang / Tinggi / Ekstrem
Information Level: Jelas / Parsial / Buta
  (seberapa lengkap klien menjelaskan situasi sebenarnya)

Hidden Complication:
  (fakta yang DM pegang, TIDAK diberi tahu ke pemain di awal)

Faction Hooks:
  (faksi mana saja yang punya kepentingan di sini, walau tak disebut klien)

Jika Berhasil:
Jika Gagal:
Jika Diabaikan (tak ada yang ambil):
```

Field terakhir ("Jika Diabaikan") penting khusus untuk format ini: **dunia tidak menunggu pemain**. Kalau tak ada yang ambil mission dalam waktu wajar (DM tentukan, biasanya 1-2 minggu in-world), sesuatu tetap terjadi — biasanya versi lebih buruk dari masalah itu muncul di [[Districts]] terkait, atau mission itu hilang dari papan dan jadi rumor lama.

### 5.3 Risk vs Information — Kenapa Dipisah

⚠️ **Kritik desain:** banyak sistem job board menyamakan "risk tinggi" dengan "informasi jelas" (job susah = job yang dijelaskan detail). Di sini sengaja **dipisah** karena kombinasinya menciptakan variasi rasa yang jauh lebih menarik untuk sandbox:

- **Risk Rendah + Info Buta** = job kelihatan remeh tapi ternyata nyembunyiin sesuatu (favorit untuk emergent story — lihat §7).
- **Risk Tinggi + Info Jelas** = job yang memang berat tapi predictable, cocok untuk party yang mau kerja cepat tanpa kejutan.
- **Risk Ekstrem + Info Buta** = biasanya cuma muncul di kontrak anonim, red flag yang sengaja, hook untuk pemain yang mencari petualangan besar.

---

## 6. World State System

Sistemnya harus **ringan** — DM tunggal (atau tim kecil) tidak akan sanggup menjalankan simulasi kota penuh. Prinsip: **catat hanya apa yang sudah tersentuh pemain atau relevan untuk mission mendatang.** Jangan pre-generate status untuk semua NPC/distrik yang belum disentuh.

### 6.1 Struktur di Obsidian

Satu note per distrik ([[Districts]]) dengan front-matter sederhana:

```yaml
---
danger_level: Calm | Tense | Volatile | Crisis
factions_present: [Wave Family, Scale Division]
active_threads: 
  - "Penyelundupan di Wavedock (naik ke Volatile minggu ke-3)"
unresolved_events:
  - "Party Rafi gagal cegah kebakaran gudang 7 — pemilik dendam ke Wave Family"
---
```

Ini bisa langsung dipakai dengan Dataview plugin Obsidian untuk lihat status semua distrik sekilas dari [[Dashboard]].

### 6.2 Progress Clock — untuk Konsekuensi Bertahap

Untuk thread yang butuh "makin lama makin parah" (bukan pass/fail sekali jalan), pakai **clock 4-6 segmen** per thread aktif:

```
Wave Family smuggling escalation: [●●●○○○] (3/6)
```

Tiap kali party mengabaikan/gagal menangani, DM isi 1 segmen. Tiap segmen tambahan, konsekuensi konkret muncul (lihat contoh §7). Clock penuh = eskalasi otomatis ke level distrik/kota (lihat §7). Clock ini dicatat langsung di note distrik terkait — **tidak perlu spreadsheet terpisah.**

### 6.3 Yang Dicatat DM Setiap Selesai Mission (Aftermath Log)

Format singkat, 3-5 baris, ditulis di note mission itu sendiri setelah lapor ke Switchboard:

```
## Aftermath
- World state changes: [distrik mana berubah, faksi mana naik/turun trust]
- NPC status changes: [siapa mati/pindah/berubah sikap]
- New rumors unlocked: [mission/hook baru yang sekarang bisa muncul di papan]
- Canon lock: [ringkasan 1 kalimat untuk dirujuk mission lain]
```

Field "Canon lock" inilah yang mencegah kontradiksi antar-party paralel (lihat §2.3).

### 6.4 Apa yang SENGAJA Tidak Disimulasikan

Untuk menjaga beban DM tetap rendah:
- Harga barang tidak fluktuasi otomatis dengan formula — cukup naratif ("harga di Wavedock naik karena rute Wave Family kena grebek") kalau relevan untuk hook, jangan buat tracker ekonomi penuh.
- NPC minor (non-faction-leader) tidak perlu status tracking — cukup faction-level.
- Jangan bikin "world tick" otomatis mingguan yang harus DM proses manual tiap distrik. Biarkan world state berubah **hanya sebagai reaksi ke mission yang benar-benar dimainkan** atau clock yang benar-benar terisi. Simulasi pasif tanpa pemicu pemain adalah kerja yang tidak akan pernah selesai untuk DM volunteer.

---

## 7. Emergent Campaign Structure — Contoh Konkret

Ilustrasi tangga eskalasi **Small Side Quest → Major Arc**, dengan titik keputusan pemain dan opsi berhenti di tiap tahap (player tidak wajib lanjut). Contoh ini berjalan dalam satu Party Tier (Tier I) sampai Tahap 3 — baru di Tahap 4 stakes-nya cukup besar untuk jadi Tier Transition-worthy.

### Tahap 0 — Side Quest Biasa
**Mission:** "Beberapa pekerja pelabuhan dilaporkan hilang dalam sebulan terakhir." (Kategori: Missing Person, Distrik: [[Districts#Wavedock|Wavedock]], Party Tier: I, Info Level: Parsial)

Party menyelidiki, menemukan pola: semua korban berhutang ke rentenir kecil yang ternyata jadi kaki tangan sebuah kelompok pemuja kecil yang mengklaim bisa "membayar hutang siapa pun" — dengan cara menyerahkan si peminjam sebagai persembahan ke sesuatu di gudang tua.

> **Off-ramp di sini:** kalau party cuma menyelamatkan korban yang jadi target kontrak dan tidak menggali lebih jauh, mission selesai, dibayar, selesai. Ini valid dan tidak "kurang" — dicatat cukup sebagai "gudang X dibersihkan, rentenir kabur."

### Tahap 1 — Local Problem (kalau digali)
Party menemukan kultus kecil ini ("Silent Tide") sudah beroperasi bertahun-tahun, dilindungi oleh sebagian oknum di [[Factions#The Wave Family|The Wave Family]] yang menerima setoran diam-diam.

**Pilihan pemain & konsekuensi konkret:**
- **Hancurkan kultus** → clock "Silent Tide Influence" reset, tapi oknum Wave Family yang terlibat kini memusuhi party secara personal.
- **Laporkan ke [[Factions#Scale Division|Scale Division]]** → polisi masuk, tapi lambat (butuh bukti resmi) — beri waktu kultus kabur/reorganisasi, mission baru muncul: "cari sisa kultus yang kabur."
- **Diam-diam bekerja sama** (menukar info demi bagian keuntungan) → trust dengan Wave Family naik drastis, tapi ini dicatat sebagai *unresolved event* gelap yang bisa dipakai NPC lain untuk memeras party nanti.

### Tahap 2 — Faction Conflict (kalau eskalasi)
Kalau party membongkar keterlibatan oknum Wave Family secara publik, ini memicu perpecahan internal — sebagian ingin "bersih-bersih" dan legit (selaras faksi wildcard sub-goal di [[Factions]]), sebagian mempertahankan status quo. Clock "Wave Family Internal Split" mulai berjalan di note distrik.

### Tahap 3 — District Crisis (kalau clock penuh / diabaikan lama)
Kalau tak ada party (Tier I mana pun) yang menangani Tahap 2 dalam waktu wajar, perpecahan meledak jadi kekerasan terbuka di Wavedock. `danger_level` distrik naik ke **Crisis**. Mission baru otomatis muncul di papan: Protection, Extraction, Negotiation — semua Party Tier I, terkait krisis ini, tersedia untuk party manapun, bukan cuma yang mulai thread ini.

### Tahap 4 — City-wide Crisis (opsional, hanya kalau memang dibiarkan jauh, bisa jadi Tier Transition mission)
Kalau tak ada party yang menangani Tahap 3 dalam waktu wajar, kekosongan kekuasaan di pelabuhan menarik perhatian faksi luar (bisa jadi kesempatan [[Factions#Adikarsa Group|Adikarsa Group]] mengambil alih akses pelabuhan secara "sah", memicu ketegangan baru dengan [[Factions#The Beacon Circle|The Beacon Circle]] soal pekerja lokal yang tersingkir). Skala ini cukup besar untuk dijadikan **Tier Transition Mission** resmi (§2.2) — menyelesaikannya jadi syarat naik ke Tier II.

> **Penting:** eskalasi ini **tidak wajib terjadi**. Kalau satu party menuntaskan Tahap 0 dan tidak ada party lain yang menyentuh benang ini lagi, dia tetap side quest selamanya. Eskalasi hanya jalan kalau ada pemicu nyata (pilihan pemain atau clock penuh karena diabaikan) — bukan timer otomatis dari DM.

---

## 8. Design Philosophy & Ringkasan Kritik

Prinsip inti yang harus dipegang tiap kali menambah sistem baru ke campaign ini:

1. **Player-driven, bukan plot-driven.** NPC boleh punya opini kuat, tapi tidak pernah "memberi tahu jawaban benar."
2. **Setiap sistem harus lulus tes "DM volunteer capek jam 11 malam bisa jalankan ini?"** Kalau jawabannya butuh spreadsheet rumit, sistemnya terlalu berat — sederhanakan.
3. **Tidak semua mission harus penting.** Sengaja sisakan proporsi besar mission board sebagai job murni ("anjing hilang", "antar paket") tanpa hook tersembunyi sama sekali — supaya pemain tidak paranoid curiga setiap job pasti ada konspirasi, yang justru membunuh rasa penasaran itu sendiri.
4. **Konsekuensi harus konkret dan bisa dirasakan**, bukan sekadar deskriptif ("kota jadi lebih gelap") — selalu terjemahkan ke: mission baru, NPC yang berubah sikap, atau akses yang berubah.

### Ringkasan Kritik yang Sudah Ditangani di Dokumen Ini

| Ide awal / potensi masalah | Masalah | Solusi yang dipilih |
|---|---|---|
| Leveling bebas ala West Marches klasik | Party mismatch parah di async PbP | **Party Tier** hard-gated per mission (§2.2) |
| Reputation sebagai skor tunggal | Overhead bookkeeping, gampang diabaikan | Trust Tier kualitatif per faksi (§4.4), terpisah dari Party Tier |
| World state sebagai simulasi kota penuh | Tidak sustainable untuk DM volunteer | Reaktif-only, dicatat per distrik yang tersentuh saja (§6.4) |
| Mission board dengan hidden complication kompleks per job | Beban prep tinggi kalau semua job "penting" | Mission Card ringkas + eksplisit sebagian besar job memang biasa saja (§8.3) |
| Party paralel bisa saling kontradiksi | Async + world persisten = risiko nyata, bukan teoretis | Canon Lock rule (§2.3, §6.3) |
| Eskalasi emergent tanpa batas | Bisa jadi obligasi tak berujung buat DM | Eskalasi hanya lewat clock/pilihan nyata, selalu ada off-ramp (§7) |
| Kontrak anonim gatekeeping konten dari pemain baru | Trust Tier tinggi bisa bikin pemain baru merasa tak bisa akses apa-apa | Sebagian besar mission board tetap Tier "Unknown" — anonim/tinggi cuma sebagian kecil, bukan mayoritas (§5) |

---

## Selanjutnya

Dokumen ini sengaja berhenti di struktur sistem. Setelah disetujui/direvisi, tahap berikut: starter missions (2-3 contoh lengkap pakai Mission Card template) dan contoh log Aftermath yang menunjukkan world state benar-benar berubah.

Lihat detail entitas di [[Factions]] dan [[Districts]].
