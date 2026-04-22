# DonorFlux-Evaluator (FuzzyExpert AI)

**DonorFlux Evaluator** adalah aplikasi web berbasis **Logika Fuzzy** yang mengkalkulasi tingkat kelayakan donor darah melalui evaluasi parameter medis. Sistem ini menggunakan mesin inferensi **Fuzzy Sugeno** untuk mengonversi input parameter fisik menjadi skor kelayakan absolut (0-100%).

> **Responsi Praktikum Kecerdasan Buatan** - Implementasi Fuzzy Logic untuk evaluasi kesehatan donor

---

## Fitur Utama

- **Inferensi Fuzzy Sugeno** - Mesin kalkulasi presisi menggunakan scikit-fuzzy
- **3 Parameter Input** - Hemoglobin (Hb), Tekanan Sistolik, dan Durasi Tidur
- **Skor Kelayakan 0-100%** - Output terukur dengan status definitif
- **UI Modern** - Interface responsif dengan Tailwind CSS dan animasi interaktif
- **Validasi Input Real-time** - Feedback visual untuk setiap parameter
- **Unit Testing** - Script `fuzzyTest.py` dengan 9 test cases predefinisi

---

## Parameter Evaluasi

### 1. **Kadar Hemoglobin (Hb)** 
- **Rentang:** 10 - 20 g/dL
- **Standar PMI:** 12,5 - 17,0 g/dL (Normal)
- **Fungsi Keanggotaan:** Rendah, Normal, Tinggi

### 2. **Tekanan Sistolik** 
- **Rentang:** 70 - 200 mmHg
- **Standar Aman:** 90 - 160 mmHg (Normal)
- **Fungsi Keanggotaan:** Rendah, Normal, Tinggi

### 3. **Pola Istirahat (Tidur)** 
- **Rentang:** 0 - 12 Jam
- **Standar Minimum:** 4 Jam sebelum donor
- **Fungsi Keanggotaan:** Kurang (<4 jam), Cukup (≥4 jam)

---

## Output Status

| Skor | Status | Warna |
|------|--------|-------|
| < 40 | **Tidak Layak** ❌ | Merah |
| 40 - 59 | **Tunda / Perlu Pemeriksaan** ⚠️ | Kuning |
| ≥ 60 | **Layak** ✅ | Hijau |

---

## Teknologi Stack

- **Backend:** Flask 2.x + Python 3.8+
- **Fuzzy Logic:** scikit-fuzzy (skfuzzy)
- **Frontend:** HTML5, Tailwind CSS 3, JavaScript
- **Server:** Flask Development Server (Port: 5055)
- **Typography:** Google Fonts (Plus Jakarta Sans, Space Grotesk)

---

## Struktur Direktori

```
DonorFlux-Evaluator/
├── app.py                 # Flask Application & Routes
├── fuzzyLogic.py          # Mesin Inferensi Fuzzy Sugeno
├── fuzzyTest.py           # Unit Testing & Test Cases
├── templates/
│   ├── index.html         # Halaman Beranda
│   └── fuzzy.html         # Halaman Kalkulator Fuzzy
├── README.md              # Dokumentasi
└── __pycache__/           # Cache Python
```

---

## Instalasi & Setup

### Prerequisites
- Python 3.8 atau lebih tinggi
- pip (Python Package Manager)

### Langkah Instalasi

```bash
# 1. Clone repository
git clone https://github.com/Pancar-ws/DonorFlux-Evaluator.git
cd DonorFlux-Evaluator

# 2. Install dependencies
pip install -r requirements.txt
# atau manual:
pip install flask scikit-fuzzy numpy

# 3. Jalankan aplikasi
python app.py

# 4. Buka di browser
# http://localhost:5055
```

---

## Panduan Penggunaan

### Halaman Beranda (`/`)
- Deskripsi umum sistem
- Penjelasan 3 parameter PMI
- Tombol akses ke halaman kalkulator

### Halaman Fuzzy (`/fuzzy`)
1. **Input Parameter**
   - Masukkan nilai Hemoglobin (10-20 g/dL)
   - Masukkan tekanan sistolik (70-200 mmHg)
   - Masukkan durasi tidur (0-12 jam)
   
2. **Validasi**
   - Sistem otomatis mendeteksi input invalid
   - Tampilan error field berwarna merah
   
3. **Hasil**
   - Skor kelayakan (0-100%)
   - Status dengan indikator warna
   - Opsi untuk kalkulasi ulang

---

## Logika Fuzzy Rules

Sistem menggunakan **12 fuzzy rules** untuk inferensi:

```
Rule 1: Jika Hb NORMAL AND Sistolik NORMAL AND Tidur CUKUP → Kelayakan TINGGI
Rule 2: Jika Hb RENDAH → Kelayakan RENDAH
Rule 3: Jika Hb TINGGI → Kelayakan RENDAH
Rule 4: Jika Sistolik RENDAH → Kelayakan RENDAH
Rule 5: Jika Sistolik TINGGI → Kelayakan RENDAH
Rule 6: Jika Hb NORMAL AND Sistolik NORMAL AND Tidur KURANG → Kelayakan SEDANG
Rule 7: Jika Hb RENDAH AND Sistolik NORMAL → Kelayakan RENDAH
Rule 8: Jika Hb NORMAL AND Sistolik TINGGI → Kelayakan SEDANG
Rule 9: Jika Hb TINGGI AND Sistolik NORMAL → Kelayakan SEDANG
Rule 10: Jika Hb RENDAH AND Tidur KURANG → Kelayakan RENDAH
Rule 11: Jika Hb NORMAL AND Tidur CUKUP AND Sistolik RENDAH → Kelayakan SEDANG
Rule 12: Jika Hb NORMAL AND Tidur CUKUP AND Sistolik TINGGI → Kelayakan SEDANG
```

---

## File Dokumentasi

### `app.py`
- Routes Flask untuk halaman beranda (`/`) dan kalkulator (`/fuzzy`)
- POST handler untuk pemrosesan input fuzzy menggunakan `evaluasi_fuzzy()`
- Error handling untuk input yang tidak valid
- Color coding berdasarkan status output (merah/kuning/hijau)

### `fuzzyLogic.py`
- Fungsi `evaluasi_fuzzy()` - Kalkulasi skor, status, dan warna output
- Membership functions untuk setiap input/output
- Mengembalikan tuple (score, status, warna)

### `templates/index.html`
- Landing page dengan branding "FuzzyExpert AI"
- Info box untuk parameter PMI
- CTA button ke halaman kalkulasi

### `templates/fuzzy.html`
- Form input dengan validasi real-time
- Display hasil dengan animasi pulse
- Sidebar informasi standar medis PMI
- Step indicator untuk progress (Evaluasi Parameter → Hasil Akhir)

### `fuzzyTest.py` 🆕
- Unit testing script untuk validasi Fuzzy Inference System
- 9 test cases predefinisi dengan skenario berbeda
- Menampilkan tabel output: Hb, Sistolik, Tidur, Score, Status, dan Ekspektasi
- Berguna untuk debugging dan verifikasi aturan fuzzy
- Jalankan dengan: `python fuzzyTest.py`

---

## Contoh Use Case

**Input:**
- Hemoglobin: 14.5 g/dL (Normal)
- Tekanan Sistolik: 120 mmHg (Normal)
- Durasi Tidur: 7 jam (Cukup)

**Output:**
- Skor: 85%
- Status: ✅ **LAYAK**
- Warna: Hijau

## Testing

### Unit Testing dengan `fuzzyTest.py`

Aplikasi dilengkapi dengan script testing otomatis yang berisi 9 test cases:

```bash
python fuzzyTest.py
```

**Output Format:**
```
Hb    | Sis   | Tidur | Score  | Status                    | Ekspektasi
------|-------|-------|--------|---------------------------|-------------------
14.0  | 115   | 8     | 85.23  | Layak                     | [Sangat Layak]
14.0  | 115   | 3     | 52.10  | Tunda / Perlu Pemeriksaan | [Dipertimbangkan]
11.0  | 115   | 8     | 25.50  | Tidak Layak               | [Tidak Layak]
...
```

**Test Cases Mencakup:**
- ✅ Skenario ideal (Hb normal, Sistolik normal, Tidur cukup)
- ⚠️ Skenario borderline (edge cases dengan nilai ambang)
- ❌ Skenario tidak layak (parameter di bawah standar)
- 🤔 Skenario overlap (validasi membership function)

---