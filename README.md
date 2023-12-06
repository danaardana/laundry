
# Laundry 

Aplikasi berbasis CMD untuk laundry bojong dan laundry soang, sebagai bentuk implementasi Publish-Subscribe.



## Deployment

Menjalankan aplikasi dilakukan dengan cara unduh dan salin pada tools yang digunakan seperti XAMPP

<details>

<summary>Konfigurasi Database</summary>

### Setup Database
Pastikan XAMPP dapat digunakan dengan sempurna, selanjutnya
1. Jalankan modul Apache dan MySQL
2. Tekan admin pada modul MySQL
3. Pilih import

</details>



## Features

- Pengecekan menu pilihan
- Implementasi CRUD MySQL
- Implementasi Publish-Subscribe
- Publish pembaharuan informasi bila laundry telah selesai
- Opsi pemesanan cabang laundry
- Menyediakan broadcast informasi





## Tabel Pada Database

Berikut adalah list table yang digunakan

| Table |Type| Description |
| --- | --- |--- |
| id | varchar(10) | Mengandung angka dana huruf, bersifat unik |
| cabang | varchar(10) | - |
| name | varchar(10) | Tidak boleh mengandung angka |
| berat | int | - |
| harga | int | - |
| tgl_selesai | varchar(10) | Menggunakan varchar agar memudahkan pengolahan data |
| status | tinyint(1) | Status laundry dapat diubah manual pada menu 3 |# laundry
Implementation of publish-subscribe
