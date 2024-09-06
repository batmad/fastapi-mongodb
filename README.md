# Belajar FastAPI dengan MongoDB

Proyek ini dibuat sebagai bagian dari proses belajar saya dalam menggunakan **FastAPI** dengan **Python** dan menghubungkannya ke database **MongoDB**. Proyek ini fokus pada pemahaman konsep dasar seperti koneksi database, pembuatan API, dan operasi CRUD.

## Persyaratan

Sebelum memulai, pastikan perangkat berikut telah terinstal:

- Python 3.7+
- MongoDB
- `pip` (Package manager Python)

## Tujuan Pembelajaran

1. **Mempelajari FastAPI**: Menggunakan FastAPI untuk membuat API yang ringan dan cepat.
2. **Koneksi ke MongoDB**: Menghubungkan aplikasi Python dengan MongoDB menggunakan `pymongo`.
3. **Operasi CRUD**: Membuat, membaca, dan menampilkan data pengguna dari database MongoDB.

## Langkah Setup

1. **Clone Repositori**:
   
   Ini adalah langkah pertama untuk mengambil kode proyek.

   ```bash
   git clone https://github.com/batmad/fastapi-mongodb.git
   cd fastapi-mongodb
   ```

2. **Buat dan Aktivasi Virtual Environment**:

   Untuk memisahkan lingkungan kerja Python agar tidak bercampur dengan instalasi sistem.

   ```bash
   python -m venv venv
   source venv/bin/activate  # Di Windows gunakan `venv\Scripts\activate`
   ```

3. **Instal Dependencies**:

   Instal paket yang diperlukan untuk menjalankan aplikasi ini.

   ```bash
   pip install fastapi pymongo pydantic python-dotenv uvicorn
   ```

4. **Konfigurasi Variabel Lingkungan**:

   Buat file `.env` di root proyek dan tambahkan string koneksi MongoDB.

   ```bash
   MONGO_CONN=mongodb://localhost:27017
   ```

5. **Menjalankan Aplikasi**:

   Gunakan `uvicorn` untuk menjalankan server FastAPI dan mulai belajar dari sini.

   ```bash
   uvicorn main:app --reload --port 8001
   ```

   Server akan berjalan di `http://127.0.0.1:8001`.

## API yang Dipelajari

### 1. Mencari Pengguna Berdasarkan Username

- **Endpoint:** `/find`
- **Metode:** `GET`
- **Request Body:**
  ```json
  {
    "username": "your_username"
  }
  ```

### 2. Membuat Pengguna Baru

- **Endpoint:** `/create`
- **Metode:** `POST`
- **Request Body:**
  ```json
  {
    "nama": "Nama Lengkap",
    "username": "username"
  }
  ```

### 3. Menampilkan Semua Pengguna

- **Endpoint:** `/users`
- **Metode:** `GET`

## Kesimpulan

Proyek ini adalah langkah awal saya dalam memahami bagaimana membangun API menggunakan FastAPI dan menghubungkannya dengan MongoDB. Dengan melakukan langkah-langkah ini, saya berharap bisa lebih memahami cara kerja backend yang modern dan efektif.

Saya akan terus mengembangkan dan memperbaiki proyek ini seiring dengan perkembangan pembelajaran saya.
