# 🚲 Bike Sharing Dashboard

Dashboard ini dibuat untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti hari, jam, dan kondisi cuaca.

## 📌 Fitur Dashboard:
- **Filter Data Berdasarkan Tanggal** 📆
- **Visualisasi Penyewaan Sepeda Berdasarkan Hari & Jam** 📊
- **Statistik Data Penyewaan Sepeda** 🔍

## 🚀 Cara Menjalankan

1. Pastikan sudah menginstal **Python** dan **Streamlit**.
2. Jalankan perintah berikut di terminal:

   ```bash
   pip install streamlit pandas plotly
   streamlit run dashboard.py
   ```

3. Dashboard akan muncul di browser.

## 📊 Dataset

Dataset yang digunakan adalah **gabungan_day_hour.csv** yang berisi informasi penyewaan sepeda berdasarkan berbagai faktor seperti:
- **Tanggal (dteday)**
- **Hari dalam Seminggu (weekday)**
- **Jumlah Penyewa Sepeda (cnt)**
- **Jam Penyewaan (hr)**

## 🔧 Cara Kerja
Dashboard ini memungkinkan pengguna untuk:
1. **Memilih Tahun** - Menggunakan sidebar untuk memilih tahun tertentu.
2. **Memilih Rentang Tanggal** - Memfilter data dalam rentang 1 minggu.
3. **Memilih Hari dalam Seminggu** - Memilih hari tertentu untuk analisis lebih dalam.

Dashboard menampilkan:
- **Tren Penyewaan Sepeda per Hari** menggunakan diagram batang.
- **Jumlah Penyewaan Berdasarkan Jam** dengan diagram garis.
- **Jam dengan Penyewaan Terbanyak** ditampilkan dalam teks.


