# Stroke Prediction App

Aplikasi **Stroke Prediction** ini dibangun menggunakan Python dan Kivy, dan memprediksi kemungkinan seseorang mengalami stroke berdasarkan input yang diberikan. Aplikasi ini menggunakan model **Logistic Regression** yang telah dilatih sebelumnya untuk memberikan prediksi.

## Fitur Aplikasi

- **Input Data Pengguna**: Pengguna dapat memasukkan informasi seperti usia, tekanan darah, riwayat penyakit jantung, indeks massa tubuh (BMI), serta kebiasaan merokok.
- **Prediksi Stroke**: Setelah memasukkan data, aplikasi akan memberikan hasil prediksi apakah pengguna kemungkinan mengalami stroke.
- **Antarmuka yang Sederhana**: Dibangun dengan menggunakan **Kivy**, antarmuka aplikasi ini bersih dan responsif, cocok untuk digunakan di berbagai ukuran layar.

## Persyaratan

Untuk menjalankan aplikasi ini, Anda memerlukan:

- **Python 3.x**
- **Kivy**: Framework yang digunakan untuk membuat GUI aplikasi.
- **Pandas**: Untuk manipulasi data tabular.
- **Joblib**: Untuk memuat model machine learning yang sudah disimpan.

### Instalasi Kivy

Anda bisa menginstal Kivy menggunakan pip:

```bash
pip install kivy
```

### Instalasi Dependensi Lainnya

Instal dependensi lainnya dengan:

```bash
pip install pandas joblib
```

## Menjalankan Aplikasi

1. Clone repositori ini ke lokal Anda:

```bash
git clone https://github.com/username/stroke-prediction-app.git
```

2. Pastikan Anda memiliki file **logistic_model_stroke_web.pkl** di direktori utama. Ini adalah file model Logistic Regression yang telah dilatih. Anda bisa melatih model sendiri atau menggunakan model yang sudah ada.

3. Jalankan aplikasi dengan perintah:

```bash
python logistic_model_stroke_app.py
```

## Cara Menggunakan

1. Buka aplikasi.
2. Masukkan data pengguna di bidang yang tersedia:
   - **Umur**: Umur pengguna (misalnya 45.5).
   - **Hipertensi**: Apakah pengguna memiliki riwayat hipertensi (Ya/Tidak).
   - **Penyakit Jantung**: Apakah pengguna memiliki riwayat penyakit jantung (Ya/Tidak).
   - **Glukosa Rata-rata**: Nilai rata-rata glukosa darah pengguna (misalnya 85.3).
   - **BMI**: Indeks Massa Tubuh (misalnya 24.6).
   - **Jenis Kelamin**: Laki-laki, Perempuan, atau Lainnya.
   - **Status Pernikahan**: Apakah pengguna pernah menikah (Ya/Tidak).
   - **Pekerjaan**: Pekerjaan pengguna saat ini (Swasta, Wiraswasta, Tidak Pernah Bekerja, Anak-anak).
   - **Tempat Tinggal**: Tipe tempat tinggal pengguna (Perkotaan/Pedesaan).
   - **Status Merokok**: Apakah pengguna pernah merokok, tidak pernah merokok, atau masih merokok.
3. Klik tombol **Prediksi** untuk melihat hasil prediksi.
4. Hasil prediksi akan ditampilkan di bagian bawah aplikasi.

## Model Machine Learning

Model machine learning yang digunakan adalah **Logistic Regression** yang telah dilatih untuk memprediksi kemungkinan stroke berdasarkan data dari pengguna. Model ini menggunakan fitur-fitur berikut:
- **Umur**
- **Tekanan Darah Tinggi (Hipertensi)**
- **Riwayat Penyakit Jantung**
- **Glukosa Rata-rata**
- **BMI**
- **Jenis Kelamin**
- **Status Pernikahan**
- **Pekerjaan**
- **Tempat Tinggal**
- **Status Merokok**
