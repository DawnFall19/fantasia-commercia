---
title: README

---

LINK: http://michael-ignasius-fantasiacommercia.pbp.cs.ui.ac.id/

Jawaban:
1. Step by step:
    1. Membuat <i>virtual environment</i> yang baru kemudian mengaktifkannya.
    2. Membuat `requirements.txt` yang berisi <i>depencencies</i> yang dibutuhkan.
    3. Membuat proyek Django baru.
    4. Menambahkan <i>local host</i> ke `settings.py` agar hasil dapat ditampilkan melalui <i>local host</i>.
    5. Membuat <i>repository</i> baru di GitHub dan menghubungkannya dengan <i>repository</i> lokal yang telah dibuat.
    6. Membuat berkas `.gitignore` yang akan membuat Git mengabaikan berkas yang tidak diperlukan ketika akan melakukan <i>4 Git Mantras</i> (<i>Add, Commit, Push, Pull</i>).
    7. Mendaftarkan proyek pada PWS.
    8. Membuat aplikasi baru bernama `main`.
    9. Menambahkan `main` ke dalam `settings.py` pada bagian `INSTALLED_APPS`.
    10. Membuat berkas HTML `main.html`.
    11. Menambahkan judul, nama, NPM, dan kelas ke dalam `main.html`.
    12. Membuat model baru pada `models.py`.
    13. Melakukan migrasi agar dapat mengaplikasikan model baru.
    14. Menambahkan fungsi untuk menghubungkan `views.py` dengan `templates`.
    15. Melakukan konfigurasi routing pada `urls.py` di dalam `main`.
    16. Melakukan konfigurasi routing proyek pada `urls.py` di dalam `fantasia-commercia`.
    17. Membuat dan menjalankan tes pada `tests.py`.
    18. Melakukan <i>4 Git Mantras</i> untuk menyimpan hasil ke dalam GitHub.

2. 
![Bagan Arsitektur Django](https://github.com/DawnFall19/fantasia-commercia/blob/main/bagan_django.jpeg)
- urls.py: Memetakan URL ke fungsi views yang sesuai.
- views.py: Menangani logika aplikasi dan mengatur interaksi dengan model serta template.
- models.py: Mewakili tabel dalam database dan berfungsi untuk operasi database.
- Template (HTML): Menampilkan data yang dikirim oleh views dalam bentuk halaman web yang bisa dilihat pengguna.

3. - Kontrol Versi
    Git memungkinkan pemilik dan pengembang untuk memantau dan mengetahui setiap perubahan yang terjadi pada suatu proyek.
    - Kolaborasi
    Git memungkinkan sebuah proyek untuk dibagikan dan dikerjakan oleh lebih dari satu orang tanpa mengganggu pekerjaan satu sama lain.
    - Branching and Merging
    Git memungkinkan setiap pengembang dalam tim untuk memiliki tempat kerjanya sendiri yang tidak mengganggu pekerjaan rekannya dengan membuka cabang baru dan ketika cabang telah selesai dikerjakan dan diterima, cabang dapat digabungkan ke dalam kode utama.
    - Resolusi Konflik
    Git memungkinkan penyelesaikan konflik yang biasanya terjadi ketika beberapa pengembang mengubah bagian kode yang sama sehingga Git memiliki kesulitan tentang kode mana yang harus digabungkan dengan kode utama.
    
4. Terdapat 2 alasan utama yang saya temukan, yang pertama adalah karena Django menggunakan salah satu bahasa pemrograman yang sangat <i>user-friendly</i> dan <i>newbie-friendly</i> yaitu Python. Dan yang kedua adalah karena banyaknya fitur dan fungsi yang dimiliki Django sehingga memudahkan pemula untuk menggunakannya tanpa terlalu banyak mengubah atau mengatur konfigurasi.

5. Terdapat beberapa alasan, yaitu:
    - Django memungkinkan developer untuk bekerja dengan data dalam bentuk objek Python, sementara di belakang layar, ORM akan mengonversi operasi-operasi pada objek tersebut menjadi query SQL untuk berinteraksi dengan database. Ini menyederhanakan akses ke database dan meminimalkan kebutuhan untuk menulis SQL.
    - Dalam Django, setiap class model merepresentasikan tabel di database dimana setiap atribut mewakili kolom dalam tabel tersebut. Dengan cara ini, setiap instance dari model adalah representasi dari baris data dalam tabel.
    - Dengan menggunakan Django, operasi seperti menambah, mengubah, menghapus, atau mengambil data dapat dilakukan tanpa menulis SQL langsung. ORM secara otomatis mengubah operasi tersebut menjadi query SQL yang sesuai.
    - Django bersifat database-agnostic, artinya dapat digunakan dengan berbagai jenis database relasional (seperti PostgreSQL, MySQL, SQLite, dll.) tanpa harus menulis query SQL yang spesifik untuk tiap database. ORM yang mengurus konversi query SQL yang sesuai untuk database yang digunakan.