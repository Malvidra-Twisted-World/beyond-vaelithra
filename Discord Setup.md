# Discord Setup — Beyond Vaelithra

> Terkait: [[Design Document]] · [[Starter Missions]] · [[Dashboard]]

Tiga hal siap pakai: struktur channel, draft pengumuman pembukaan, dan pinned rules. Semua teks di bawah sudah dalam format Markdown Discord — tinggal copy-paste.

---

## 1. Struktur Channel & Role

Server kamu ("D&D with Malvidra") sudah pakai konvensi **satu category per campaign** — KARTALOKA sudah ada. Jadi tidak perlu bikin 3 category terpisah kayak draft awal; cukup semua channel di bawah ini masuk **satu category KARTALOKA** yang sudah ada, dan mission pakai **thread** (bukan channel baru tiap mission) supaya sidebar tidak numpuk kayak yang lain.

### Category: 📖 KARTALOKA (sudah ada — tinggal isi channel)
| Channel | Fungsi | Fixer bisa chat? |
|---|---|---|
| `#welcome-rules` | Pinned rules (§3 di bawah) — setara `#what-to-know` di campaign lain kamu | Tidak (view + react) |
| `#the-switchboard` | Papan kontrak. Kamu post Mission Card, player **react** buat klaim | Tidak (view + react) |
| `#signal-feed` | "Berita kota" — update world state publik + Canon Lock summary tiap mission closed | Tidak (view + react) |
| `#character-sheets` | Sheet + status Party Tier tiap karakter | Ya |
| `#old-town-lounge` | RP bebas ala kedai kopi Ibu Tumini — tempat party kebentuk organik | Ya |

### Alur Klaim Mission (menyesuaikan `#the-switchboard` read-only)

Karena Fixer cuma bisa view + react di `#the-switchboard`, klaim mission jalan lewat reaction, bukan reply/chat:

1. Kamu post Mission Card sebagai satu message.
2. Player yang minat **react** ke message itu (misal 🖐️) — semacam "raise hand" buat ambil job.
3. Setelah party kebentuk (kamu yang putuskan siapa gabung, cek dulu Party Tier-nya cocok), kamu bikin **thread** dari message Mission Card itu dan invite/add player yang react.
4. Mission jalan di dalam thread — thread otomatis punya izin chat sendiri walau parent channel read-only, jadi player bisa ngobrol normal di situ.

> **Narrative framing:** kebetulan pas — proses ini bisa dijelaskan in-fiction sebagai Wulan yang meninjau siapa yang react/berminat, lalu "menyetujui" dan resmi menugaskan kontrak itu ke party (buka jalur komunikasi khusus buat mereka). Jadi thread baru bukan cuma solusi teknis izin Discord, tapi juga step naratif: **kontrak belum resmi jadi milik party sampai Wulan buka jalurnya.** Ini bisa jadi hook kecil juga — kalau Wulan menahan approval, itu tandanya ada yang janggal soal party atau kliennya.

Naming convention thread:

```
[T1] Wavedock — The Silent Tide
[T1] Beacon District — Piyah Belum Pulang
```

Format: `[Tier] Distrik — Judul Mission`. Selesai mission → thread di-archive (bukan dihapus), tetap bisa dirujuk buat Canon Lock.

> **Catatan:** kalau ternyata role Fixer juga tidak punya izin "Create Threads" di channel itu (bukan cuma "Send Messages"), thread tetap harus kamu yang buka manual seperti alur di atas — jadi aman baik izinnya ketat sekalian atau tidak.

### Role
| Role | Untuk apa |
|---|---|
| `Dungeon Master` | Role admin kamu yang sudah ada — pegang Dashboard, world state, dan keputusan Canon Lock |
| `Fixer` | Role dasar semua player PbP — bikin baru, khusus dipakai buat bedain dari player campaign lain di server kamu |
| `Tier I` / `Tier II` / `Tier III` / `Tier IV` | Bikin baru, nempel manual (atau lewat reaction role) pas karakter naik tier — dipakai buat gampang lihat siapa boleh klaim mission tier berapa di `#the-switchboard` |

---

## 2. Draft Pengumuman Pembukaan

Post ini di channel pengumuman utama server (bukan `#welcome-rules` — itu isinya rules statis).

```
🏙️ **KARTALOKA IS OPEN**

Kartaloka — kota pelabuhan terbesar di Dewanegara, beberapa abad setelah Sundering War.
Bukan dungeon crawl. Bukan satu plot besar yang harus diikuti semua orang.

Di sini kalian jadi **fixer** — orang yang ambil kontrak lewat **The Switchboard**, sebuah
jaringan broker netral yang menempati bekas menara radio di Old Town. Klien bisa siapa
saja: warga biasa, korporat, polisi, bahkan sindikat kriminal. Kalian pilih sendiri mau
kerja untuk siapa.

**Cara main:**
1. Buat karakter **Tier I** (level 1-4) — cek `#character-sheets` untuk template.
2. Cek `#the-switchboard` untuk mission yang tersedia buat tier kalian.
3. **React** ke Mission Card yang kalian minat (🖐️) buat "raise hand" ambil job — DM
   bakal bikin thread dan invite kalian begitu party kebentuk.
4. Main **santai** — tidak ada kewajiban posting harian. Thread boleh pause kalau ada
   yang offline, lanjut kapan aja.
5. Selesai mission → lapor balik ke The Switchboard. Dunia Kartaloka **ingat** apa yang
   kalian lakukan — keputusan kalian bisa mengubah nasib distrik, bukan cuma reward XP.

Tiga mission pertama sudah nongol di `#the-switchboard`. Baca `#welcome-rules` sebelum
mulai, terus langsung gas.

Selamat datang di Kartaloka. Semoga kontrak kalian menguntungkan. 🌊
```

---

## 3. Pinned Rules (`#welcome-rules`)

```
📌 **ATURAN MAIN — KARTALOKA WEST MARCHES**

**Format**
• Async, bukan sesi terjadwal. Post kapan pun kalian online, tidak ada kewajiban harian.
• Thread mission boleh `Paused` kalau ada player offline — lanjut kapan aja mereka balik.
• Party dibentuk bebas per-mission, TAPI harus **satu Party Tier yang sama** (lihat di
  bawah) — ini hard rule, bukan saran.

**Party Tier**
• Tier I (Lv 1-4) → Tier II (Lv 5-10) → Tier III (Lv 11-16) → Tier IV (Lv 17-20).
• Karakter naik level lewat milestone per mission/arc selesai, TAPI mentok di batas atas
  tier-nya sampai selesaikan **Tier Transition Mission** (mission capstone khusus, ditandai
  jelas di board).
• Karakter baru selalu mulai di Tier I, kecuali ada alasan naratif khusus (tanya DM).

**Cara Ambil Mission**
• `#the-switchboard` read-only buat kalian — react ke Mission Card yang diminati, jangan
  chat di situ.
• Dungeon Master bikin thread dan invite kalian begitu party kebentuk. Ngobrol/main
  jalan di dalam thread itu.

**Dunia Persisten**
• Hasil mission itu permanen. Gagal ya gagal — tidak ada reset.
• Kalau mission tidak ada yang ambil dalam waktu wajar, dunia tetap jalan tanpa kalian
  (biasanya jadi lebih runyam).
• Satu thread mission yang sudah closed = canon. Jangan kontradiksi hasil mission lain
  yang sudah closed — cek `#signal-feed` atau tanya Dungeon Master kalau ragu.

**Setelah Mission Selesai**
• Wajib lapor balik (in-character ke The Switchboard, out-of-character kasih tahu
  Dungeon Master biar dicatat).
• Reward, reputasi (Trust Tier per faksi), dan perubahan dunia ditentukan dari situ —
  bukan otomatis.

Ada pertanyaan? Tanya Dungeon Master kapan saja.
```

---

## 4. Character Creation — Versi Discord (Pinned di `#character-sheets`)

> Kenapa beda dari [[Character Creation Guidelines]]: Discord tidak render markdown table, jadi versi ini diubah ke bullet list dan dipecah jadi beberapa pesan supaya tidak kena limit ~2000 karakter per message. Pin semua pesan di bawah secara berurutan.

### Pesan 1/4 — Starting Point & Race

```
📋 **BIKIN KARAKTER — START HERE**

**Starting Point**
• Level 3, class + subclass bebas pilih.
• Party Tier otomatis Tier I (Lv 1-4).
• Trust Tier semua faksi mulai `Unknown`, kecuali background kalian kasih bonus
  (lihat pesan 3/4).

**Race — seberapa lumrah di Kartaloka**
• **Umum banget:** Human, Half-Elf, Half-Orc, Tiefling (tiefling bukan hal aneh di
  kota ini, sudah biasa).
• **Cukup umum:** Dwarf & Gnome — banyak kerja di sektor engineering/finance.
• **Ada tapi minoritas:** Elf, Halfling — biasanya akademik atau ekspatriat.
• **Jarang, butuh 1-2 kalimat alasan:** Dragonborn, Aasimar, Genasi — kenapa mereka
  jauh dari kampung "khas fantasy" dan berakhir di kota industri modern?
• **Butuh approval DM dulu:** race yang berat sisi supernatural/non-humanoid
  (Changeling, Shifter, Warforged, fiend-blooded berat). Bukan dilarang, tapi
  kehadiran mereka otomatis menarik perhatian Script Order/Scale Division in-world
  — diskusikan dulu biar jadi hook, bukan cuma reskin.
```

### Pesan 2/4 — Class & Status Lisensi Caster

```
🎭 **CLASS — REFLAVOR NARATIF (mekanik tidak berubah)**

• **Fighter** — eks-militer, kontraktor keamanan, penegak hukum lepas.
• **Rogue** — pencuri jalanan, eks-hacker, informan sindikat.
• **Wizard/Sorcerer/Warlock** — WAJIB tentukan Licensed/Unlicensed (lihat bawah).
• **Cleric** — rohaniwan aktif atau chaplain rumah sakit.
• **Druid** — jarang di pusat kota, cocok dari The Fringe atau luar kota.
• **Bard** — performer klub, jurnalis, atau negosiator.
• **Ranger** — bounty hunter, penjaga pinggiran kota.
• **Monk** — praktisi dojo/sasana tradisional atau disiplin spiritual pribadi.
• **Paladin** — oath terikat institusi (Scale Division, Script Order, bahkan
  korporat) atau ke prinsip personal.
• **Artificer** — engineer independen atau staf R&D Adikarsa Group. Paling "at
  home" secara tema di sini.
• **Barbarian** — jarang, tapi kuat kalau ada alasan (trauma, komunitas non-urban,
  "tersentuh" fenomena Night Remnant).

⚖️ **STATUS LISENSI (wajib buat semua caster)**
• **Licensed** — terdaftar di Script Order. Mulai Trust Tier `Known` otomatis sama
  mereka. Sihir kalian sah di hukum, tapi mereka tahu kalian ada.
• **Unlicensed** — praktik diam-diam. Tidak dapat bonus trust, tapi risiko ketahuan
  pakai magic di depan umum bisa menarik perhatian Scale Division/Script Order
  (jadi hook cerita, bukan hukuman otomatis).
```

### Pesan 3/4 — Background & Trust Tier Bonus

```
🗂️ **BACKGROUND — KONEKSI KE DUNIA**

Wajib jawab 2-3 kalimat: kenapa karakter ini jadi fixer, dan lewat siapa/apa
pertama kali dengar soal The Switchboard?

Opsional, boleh pilih **satu** starting Trust Tier bonus kalau cocok sama backstory:
• Criminal/Spy → `Known` dengan The Wave Family
• Soldier/Folk Hero → `Known` dengan The Beacon Circle ATAU Scale Division
• Guild Artisan/Merchant → `Known` dengan Adikarsa Group
• Sage/Acolyte → `Known` dengan The Script Order
• Hermit/Outlander → `Known` dengan The Night Remnant (kalau relevan)
• Urchin/Charlatan → tidak dapat faction bonus, tapi kenal baik NPC hub (Ibu
  Tumini/Reno) — bagus buat RP hook

Jangan dipaksakan kalau backstory kalian tidak natural nyentuh faksi manapun.
```

### Pesan 4/4 — Equipment & Checklist

```
🎒 **EQUIPMENT — REFLAVOR, STATISTIK TETAP SAMA**

• Dagger → pisau lipat/combat knife
• Shortsword → baton taktis/machete pendek
• Longsword → machete panjang
• Light Crossbow → pistol semi-otomatis
• Hand Crossbow → pistol kompak/silenced
• Heavy Crossbow → shotgun
• Longbow → rifle jarak jauh
• Shield → rompi taktis/riot shield
• Leather/Studded Armor → jaket kulit/taktis
• Chain Shirt → rompi anti peluru ringan
• Plate/Half-Plate → riot gear lengkap (biasanya cuma masuk akal buat karakter dari
  institusi resmi)
• Component Pouch → kit reagent kecil, atau perangkat ber-ward resmi (Licensed)
• Thieves' Tools → lockpick set ATAU laptop/hacking kit kecil
• Healer's Kit → kit P3K modern

Uang tunai atau lewat app *Signal* — flavor doang, sama secara mekanik. Payout
mission otomatis masuk dompet Signal kecuali klien bayar tunai/barang.

✅ **CHECKLIST SEBELUM SUBMIT**
☐ Level 3, class + subclass dipilih
☐ Race dipilih (kalau "jarang"/"butuh approval", sudah ada alasan singkat)
☐ Caster: sudah tentukan Licensed/Unlicensed
☐ Background + 2-3 kalimat kenapa jadi fixer
☐ (Opsional) satu Trust Tier bonus dipilih
☐ Equipment direflavor sesuai konsep
☐ Post sheet lengkap di sini

Ragu soal race/class/background yang tidak ada di list? Tanya Dungeon Master dulu.
```

---

## 5. Announcement — Reaction Role (Carl-bot)

Versi announcement formal, mengikuti gaya visual yang sudah kamu pakai buat one-shot lain (small caps header, quote block scene-setting, field list) — disesuaikan buat campaign PbP terbuka (bukan one-shot berjadwal) dan dikasih baris reaction-role di bawah.

```
# _*Beyond Vaelithra: Kartaloka*_
PLAY BY POST — OPEN ENROLLMENT

> "Kartaloka tidak pernah tidur. Di balik lampu sodium dermaga, layar CCTV kantor,
> dan ward-grid yang berdenyut pelan di atas gedung kaca, kota ini menyimpan
> pekerjaan untuk siapa saja yang berani mengambilnya."
>
> "The Switchboard tidak peduli siapa kalian sebelumnya. Yang mereka peduli cuma
> satu: kontrak yang harus diselesaikan, dan dunia yang mengingat bagaimana cara
> kalian menyelesaikannya."

ɢᴀᴍᴇ sʏsᴛᴇᴍ ᴀɴᴅ ꜰᴏʀᴍᴀᴛ
*Game System:* D&D 5e (2014)
*Type of Game:* Sandbox Play-by-Post, Urban Fantasy Modern (bukan cyberpunk)
*Language:* Narasi Indonesia, RP bebas (Indonesia / English / Campursari)
*Format:* Async Play-by-Post — main kapan aja, gak ada jadwal sesi tetap
*Place:* Discord, category **KARTALOKA**

ɢᴀᴍᴇ sᴘᴇᴄɪғɪᴄᴀᴛɪᴏɴ
*Starting Level:* 3 (Party Tier I)
*Total Players:* Open pool, party per-mission 2-4 orang
*Allowed Materials:* WoTC Materials that can be easily referenced
*Ability Scores Method:* Manual via `dnd!rollstats` atau Point Buy
*Content Warning:* Kejahatan urban, occult horror ringan, moral abu-abu — full
Lines & Veils ada di `#welcome-rules`
*What to Expect:*
- Sandbox murni — tidak ada satu plot besar yang wajib diikuti semua orang
- Mission board dipilih sendiri lewat The Switchboard, dari kasus kecil sampai
  yang bisa berkembang jadi arc besar tergantung keputusan kalian
- Dunia persisten — konsekuensi mission tetap ada, tidak reset
- Party dibentuk fleksibel per-mission, cocok buat yang jadwalnya gak tentu
- Newbie friendly — panduan karakter & cara main lengkap tersedia
- Berdiri sendiri dari Vaelithra Saga — beda garis waktu, tidak wajib tahu lore itu

ʜᴏᴡ ᴛᴏ ᴊᴏɪɴ
1. React 📻 di bawah buat dapat role dan akses channel **KARTALOKA**.
2. Baca `#welcome-rules` (rules + content note) dan `#character-sheets` (panduan
   bikin karakter).
3. Submit karakter Tier I (Level 3), cek `#the-switchboard` buat mission pertama.

_Contact <@DM_USER_ID> untuk pertanyaan._

---

<@&FIXER_ROLE_ID> | react 📻 di bawah buat dapat role ini
```

**Ganti sebelum post:** `<@DM_USER_ID>` dengan mention kamu, `<@&FIXER_ROLE_ID>` dengan mention role `Fixer` yang sudah kamu buat.

### Setup Reaction Role di Carl-bot

Teks di atas cukup panjang (dekat/lewat limit 2000 karakter pesan biasa Discord). Karena ini harus tetap **satu post** buat reaction role, cara paling aman:

1. Buka dashboard Carl-bot (carl.gg) → server kamu → **Reaction Roles** → buat message baru lewat fitur "Send Embed" di situ (embed limit jauh lebih longgar, ~4000-6000 karakter, cukup buat teks ini), paste seluruh isi announcement ke embed description.
2. Set emoji 📻 di reaction role itu, arahkan ke role `Fixer`.
3. Simpan & kirim — Carl-bot post embed itu ke channel pengumuman dan langsung nempelin emoji-nya.

Kalau tetap mau post sebagai pesan biasa (bukan embed) dan ternyata kena limit: potong bagian *What to Expect* jadi lebih ringkas dulu — tapi strukturnya (satu post, role-line di bagian bawah) tetap dipertahankan.

> Emoji 📻 sengaja dipilih karena nyambung ke lore Hub (Westa Tower, bekas menara radio) — boleh diganti emoji lain kalau lebih cocok sama server kamu, yang penting konsisten sama yang di-setup di Carl-bot.

---

## Status
- [x] Struktur channel & role
- [x] Draft pengumuman pembukaan
- [x] Pinned rules
- [x] Character creation — versi Discord (4 pesan siap pin)
- [x] Announcement reaction-role (Carl-bot) — siap post
- [ ] Post beneran ke Discord (manual — bagian kalian)
