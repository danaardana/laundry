
# Laundry 

Aplikasi berbasis CMD untuk laundry bojong dan laundry soang, sebagai bentuk implementasi Publish-Subscribe.



## Deployment
Tahap-tahap untuk deployment adalah sebagai berikut:
1. Pastikan database pada XAMPP telah tersedia 
2. Unduh atau clone script
3. Jalankan script server
4. Jalankan script client

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
| status | tinyint(1) | Status laundry dapat diubah manual pada menu 3 |
## FAQ

#### Kenapa menggunakan MySQL

<Jawab> Penggunaan database diperlukan untuk menyimpan data dan manipulasi data</Jawab>

#### Apa itu CRUD?

<details> CRUD singkatan dari Creat, Remove, Update, Delete. Yakni manipulasi data</details>

#### Kenapa koneksi MySQL tidak dibuat fungsi?

<details> Bedasarkan percobaan yang telah dilakukan, ketika akan melakukan koneksi menggunakan fungsi. Koneksi tersebut sudah tutup, koneksi tersebut dapat ditemui pada variable mydb.</details>

#### Apa fungsi mydb.commit()?

<details> Fungsi commit() untuk memastikan adanya perubahan pada database</details>

#### Apa fungsi sql.execute(query,value)?

<details> Fungsi untuk menjalankan perintah query, perlu dingat tidak akan ada perubahan pada database</details>

#### Kenapa saat menguhubunggkan hanya menggunakan user dan nama database?

<details> Pada implemntasi saat ini menggunakan pengaturan username dan password default sehingga tetap dapat berjalan.</details>

#### Buat apa __name__ == '__main__' ?

<details> Script itu sebenernya diperuntukan apabila file tersebut dijalankan sebagai modul, sehingga memastikan bahwa fungsi sciprt dijalankan bila file tersebut dijalankan secara tunggal.</details>
