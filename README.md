
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
- Perbaharui kode ID bila memesan ulang
- Mengirim permintaan dan menghapus pesanan





## Tabel Pada Database

Berikut adalah list table yang digunakan

| Table |Type| Description |
| --- | --- |--- |
| id | varchar(10) | Mengandung angka dana huruf, bersifat unik |
| cabang | varchar(10) | - |
| name | varchar(20) | Tidak boleh mengandung angka |
| berat | int | - |
| harga | int | - |
| tgl_selesai | varchar(10) | Menggunakan varchar agar memudahkan pengolahan data |
| status | tinyint(1) | Status laundry dapat diubah manual pada menu 3 |




## FAQ

<details>
 <summary>Buat apa __name__ == '__main__' ?</summary>
 Script itu sebenernya diperuntukan apabila file tersebut dijalankan sebagai modul, sehingga memastikan bahwa fungsi sciprt dijalankan bila file tersebut dijalankan secara tunggal.
</details>

<details>
 <summary>Kenapa menggunakan MySQL</summary>
 Penggunaan database diperlukan untuk menyimpan data dan manipulasi data
</details>

<details>
 <summary>Apa itu CRUD?</summary>
 CRUD singkatan dari Creat, Remove, Update, Delete. Yakni manipulasi data
</details>

<details> 
 <summary>Kenapa saat menguhubunggkan hanya menggunakan user dan nama database?</summary>
 Pada implemntasi saat ini menggunakan pengaturan username dan password default sehingga tetap dapat berjalan.
</details>

<details> 
 <summary>Kenapa koneksi MySQL tidak dibuat fungsi?</summary>
 Bedasarkan percobaan yang telah dilakukan, ketika akan melakukan koneksi menggunakan fungsi. Koneksi tersebut sudah tutup, koneksi tersebut dapat ditemui pada variable mydb.
</details>

<details>
 <summary>Apa fungsi mydb.commit()?</summary>
 Fungsi commit() untuk memastikan adanya perubahan pada database
</details>

<details> 
 <summary>Apa fungsi sql.execute(query,value)?</summary>
 Fungsi untuk menjalankan perintah query, perlu dingat tidak akan ada perubahan pada database
</details>

<details> 
 <summary>Mengapa menggunakan JSON?</summary>
 MQTT message payloads merupakan byte arrays, dan tidak memiliki format. Sedangkan string dapat bekerja bila memiliki tipe encoding yang sesuai. 
</details>