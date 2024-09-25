LINK: http://michael-ignasius-fantasiacommercia.pbp.cs.ui.ac.id/

# TUGAS 2
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
![Bagan Arsitektur Django](https://github.com/DawnFall19/fantasia-commercia/blob/main/Images/bagan_django.jpeg)
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

# TUGAS 3
Jawaban:
1. <i>Data delivery</i> sangat penting dalam pengimplementasian sebuah platform karena menjadi fondasi untuk menyampaikan informasi atau data dari satu titik ke titik lainnya, dengan tujuan agar platform dapat berjalan dengan baik. <i>data delivery</i> memastikan bahwa platform yang telah dibuat dapat berfungsi dengan cepat, aman, dan efisien, sekaligus mendukung interaksi pengguna yang lancar dan memastikan integrasi sistem berjalan tanpa masalah.

2. Menurutku, JSON adalah pilihan yang lebih baik dan unggul. Terdapat beberapa alasan yang mendukung pernyataan ini, antara lain:
    - JSON memiliki struktur yang lebih sederhana dan lebih ringkas dibandingkan XML. JSON tidak memerlukan tag pembuka dan penutup seperti pada XML yang membuat JSON terlihat lebih ringkas dan lebih cepat diproses.
    - Karena lebih ringkas, JSON lebih mudah dibaca dan lebih cepat ditulis. Struktur JSON lebih mudah dipahami, terutama bagi pengembang yang terbiasa dengan pemrograman berbasis objek (OOP).
    - JSON umumnya lebih cepat untuk diparse karena lebih sederhana dan tidak memiliki overhead yang besar seperti XML.

3. fungsi `is_valid()` berperan dalam melakukan validasi input yang diberikan oleh <i>user</i> melalui `form`. Validasi yang dilakukan dapat berupa tipe data, ukuran data, dan lain-lain. Melalui fungsi ini, pengembang dapat memastikan bahwa data telah sesuai aturan guna mencegah <i>error</i> internal yang dapat menyebabkan <i>crash</i> dan sebagainya.

4. `csrf_token` dalam aplikasi Django berfungsi untuk mencegah serangan yang memanfaatkan celah Cross-Site Request Forgery (CSRF). Tanpa `csrf_token`, penyerang bisa memanfaatkan sesi yang sah untuk menjalankan aksi berbahaya tanpa persetujuan atau sepengetahuan pengguna, seperti memodifikasi data, transaksi ilegal, atau bahkan mengambil alih akun pengguna. Django menggunakan `csrf_token` untuk memastikan bahwa setiap permintaan `POST` yang masuk benar-benar berasal dari sumber yang sah dan bukan dari pihak ketiga yang berbahaya. Salah satu contoh serangan CSRF adalah eksploitasi ketidakhadiran CSRF protection untuk mengubah data atau memulai transaksi yang tidak diinginkan oleh pengguna. Sebagai contoh, pada aplikasi <i>e-commerce</i>, penyerang bisa membuat pengguna tanpa sadar memproses pembelian, menambahkan barang ke keranjang, atau bahkan mengubah informasi akun pengguna.

5. Step by step:
   1. Membuat sebuah berkas bernama `forms.py` yang akan menerima entri baru dari model yang telah dibuat.
   2. Menambahkan <i>import</i> `redirect` dalam `views.py` kemudian membuat fungsi yang akan menampilkan `form` untuk menerima entri dari `user` dan menambahkan entri tersebut ke dalam data secara otomatis.
   3. Menambahkan data dari `form` ke dalam `views.py`.
   4. Menambahkan <i>import</i> terhadap fungsi yang akan menampilkan `form` pada langkah kedua ke dalam `urls.py`.
   5. Menambahkan <i>path</i> URL dari fungsi tersebut ke dalam variabel `urlpatterns` pada `urls.py`.
   6. Membuat berkas HTML dengan nama yang sama dengan fungsi yang menampilkan `form` di dalam direktori `templates` di dalam direktori `main` yang sudah dibuat pada tugas sebelumnya dimana berkas tersebut akan menjadi halaman dari `form`.
   7. Menambahkan fungsi untuk menampilkan data <i>item</i> dalam bentuk tabel dan menambahkan tombol "Add New Item Entry" yang akan mengarahkan <i>user</i> ke halaman HTML `form` yang telah dibuat.
   8. Menambahkan <i>import</i> terhadap `HttpResponse` dan `serializers` dalam `views.py`.
   9. Membuat fungsi dalam `views.py` yang akan menerima parameter <i>request</i> dan memiliki variabel yang akan menyimpan semua entri dalam `ItemEntry` lalu mengembalikan sebuah `HttpResponse` dalam bentuk XML.
   10. Membuat fungsi dalam `views.py` yang akan menerima parameter <i>request</i> dan memiliki variabel yang akan menyimpan semua entri dalam `ItemEntry` lalu mengembalikan sebuah `HttpResponse` dalam bentuk JSON.
   11. Menambahkan <i>import</i> `uuid` pada `models.py` dan membuat `id` untuk setiap <i>item</i> yang nantinya dibuat.
   12. Melakukan migrasi dengan dua baris perintah `python manage.py makemigrations` dan `python manage.py migrate`.
   13. Membuat fungsi dalam `views.py` yang akan menerima parameter <i>request</i> dan `id` serta memiliki variabel yang akan menyimpan entri dalam `ItemEntry` yang memiliki `id` tertentu lalu mengembalikan sebuah `HttpResponse` dalam bentuk XML.
   14. Membuat fungsi dalam `views.py` yang akan menerima parameter <i>request</i> dan `id` serta memiliki variabel yang akan menyimpan entri dalam `ItemEntry` yang memiliki `id` tertentu lalu mengembalikan sebuah `HttpResponse` dalam bentuk JSON.
   15. Menambahkan <i>import</i> terhadap empat buah fungsi yang telah dibuat ke dalam `urls.py` dan menambahkan `path` terhadap empat buah fungsi tersebut ke dalam variabel `urlpatterns`.

Foto XML Melalui Postman
![Penampakan XML Melalui Postman](https://github.com/DawnFall19/fantasia-commercia/blob/main/Images/xml.png)
Foto JSON Melalui Postman
![Penampakan JSON Melalui Postman](https://github.com/DawnFall19/fantasia-commercia/blob/main/Images/json.png)
Foto XML_BY_ID Melalui Postman
![Penampakan XML dengan ID Melalui Postman](https://github.com/DawnFall19/fantasia-commercia/blob/main/Images/xml_by_id.png)
Foto JSON_BY_ID Melalui Postman
![Penampakan JSON dengan ID Melalui Postman](https://github.com/DawnFall19/fantasia-commercia/blob/main/Images/json_by_id.png)

# Tugas 4
Jawaban:
1.  `HttpResponseRedirect()` adalah fungsi yang menerima URL sebagai parameter dan mengembalikan respons HTTP sedangkan `redirect()` adalah fungsi yang menerima URL atau nama view bersama parameter yang bersangkutan dan akan mengembalikan objek `HttpResponseRedirect()` sehingga `redirect()` adalah bentuk yang lebih umum dan fleksibel dibandingkan `HttpResponseRedirect()`.

2. Penghubungan model `Product` ke `User` dilakukan dengan `ForeignKey` yang digunakan untuk mendefinisikan relasi banyak-ke-satu (many-to-one). parameter `on_delete` diisi dengan `models.CASCADE` yang berarti bahwa jika seorang `User` dihapus, maka semua `Product` yang berkaitan juga dihapus.

3. <i>authentication</i> akan melakukan verifikasi pengguna ketika mencoba login, contoh paling sederhana dari <i>authentication</i> adalah melakukan verifikasi <i>username</i> dan <i>password</i>. Sedangkan <i>authorization</i> akan menentukan dan menyeleksi hal-hal yang dapat diakses oleh pengguna, contoh paling sederhana dari <i>authorization</i> adalah jumlah fitur atau bagian yang dapat diakses oleh seorang <i>admin</i> biasanya akan lebih banyak daripada <i>user</i>.

4. Menggunakan <i>cookies</i> dimana data pengguna akan disimpan ketika <i>login</i> dan dibuang ketika sesi habis atau <i>logout</i>. Contoh sederhana dari sesi yang habis adalah pengguna dari <i>website</i> SCeLe akan diberikan notifikasi sesi habis dan diarahkan ke halaman login ketika tidak melakukan apapun di dalam <i>website</i> selama beberapa waktu.

5. Step by step:
   1. Menambahkan <i>import</i> `UserCreationForm` dan `messages` ke dalam `views.py`.
   2. Membuat fungsi dalam `views.py` yang akan menghasilkan formulir registrasi secara otomatis.
   3. Membuat berkas HTML baru pada `main/templates` yang akan berisi program untuk registrasi.
   4. Menambahkan <i>import</i> terhadap fungsi yang telah dibuat ke dalam `urls.py` dan menambahkan `path` terhadap fungsi tersebut ke dalam variabel `urlpatterns`.
   5. Menambahkan <i>import</i> `AuthenticationForm`, `authenticate`, `login` dan `logout` ke dalam `views.py`.
   6. Membuat fungsi dalam `views.py` yang akan mengautentikasi pengguna yang ingin <i>login</i>.
   7. Membuat berkas <i>login</i> pada `main/templates` yang akan meminta pengguna untuk <i>login</i> sebelum dapat mengakses halaman utama.
   8. Membuat fungsi dalam `views.py` yang akan melakukan <i>logout</i> dan mengarahkan pengguna ke menu <i>login</i> kembali.
   9. Menambahkan tombol <i>logout</i> ke dalam `main.html`.
   10. Menambahkan <i>import</i> terhadap fungsi <i>login</i> dan <i>logout</i> yang telah dibuat ke dalam `urls.py` dan menambahkan `path` terhadap dua fungsi tersebut ke dalam variabel `urlpatterns`.
   11. Menambahkan <i>import</i> `login_required` ke dalam `views.py`.
   12. Menambahkan `@login_required(login_url='/login')` ke atas fungsi `show_main` pada `views.py` untuk mengharuskan pengguna login sebelum dapat mengakses halaman utama.
   13. Menambahkan <i>import</i> `HttpResponseRedirect`, `reverse`, dan `datetime` ke dalam `views.py`.
   14. Mengubah fungsi <i>login</i> pada `views.py` untuk dapat mencatat waktu <i>login</i> terakhir dari pengguna.
   15. Menambahkan informasi <i>login</i> terakhir pengguna dalam fungsi `show_main` untuk diperlihatkan.
   16. Menambahkan informasi <i>login</i> terakhir pengguna ke dalam `main.html`.
   17. Mengubah fungsi <i>logout</i> pada `views.py` untuk menghapus `cookie` ketika pengguna <i>logout</i>.
   18. Memastikan terdapat setidaknya satu <i>user</i> di dalam data, jika belum ada <i>user</i> maka perlu dibuat terlebih dahulu.
   19. Menambahkan <i>import</i> `User` ke dalam `models.py`.
   20. Menambahkan data <i>user</i> ke dalam `ItemEntry`.
   21. Mengubah fungsi `create_mood_entry` pada `views.py` yang akan menyimpan <i>user</i> yang melakukan <i>login</i>.
   22. Melakukan penyaringan entri terhadap <i>user</i> saat ini.
   23. Melakukan migrasi model.
   24. Menekan angka 1 jika muncul error, dan menekan angka 1 kembali untuk menetapkan <i>user</i> dengan ID 1 pada model yang sudah ada.
   25. Menambahkan <i>import</i> `os` ke dalam `settings.py`.
   26. Mengganti kode `DEBUG` pada `settings.py` menjadi `PRODUCTION = os.getenv("PRODUCTION", False)` dan `DEBUG = not PRODUCTION`.