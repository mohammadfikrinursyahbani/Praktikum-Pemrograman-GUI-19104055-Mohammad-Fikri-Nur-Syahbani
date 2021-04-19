# Praktikum-Pemrograman-GUI
## 19104055 Mohammad Fikri Nur Syahbani
## Installasi Software Python
## Langkah 1
Isi tanda centang yang ada pada 2 kolom lalu klik Install Now
![enter image description here](https://i.ibb.co/rmt6YWW/11.png)

## Langkah 2
Tunggu Installasi selesai

![enter image description here](https://i.ibb.co/W2yDnKv/22.png)

## Menggunakan Python Shell
Pada python anda dapat menjalankan instruksi langsung melalui Python IDLE.
Berikut adalah contoh baris intruksi yang langsung dituliskan pada IDLE

![enter image description here](https://i.ibb.co/GFSRHGM/6.png)

## Variabel dan Objek
Dibawah ini variable x awalnya berisi tipe data integer (int). Dimana
selanjutnya variable tersebut digunakan untuk menampung nilai dari tipe data lain
(bool dan str), sehingga satu variable dapat berubah-ubah tipe datanya sesuai dengan
kebutuhan

![enter image description here](https://i.ibb.co/RvpFJF5/7.png)

Dibawah ini id merupakan sebuah identitas unik yang dimiliki oleh setiap
variable. Cara mendapatkan id adalah dengan menggunakan perintah
id(‘nama_variabel’) . Untuk setiap variable jika memiliki nilai yang sama maka
python akan menunjuk nilai yang sama untuk variable yang berbeda.

![enter image description here](https://i.ibb.co/bJkp3S2/8.png)

Kode dibawah ini, jika kita memanggil id untuk variable x maupun y maka akan
muncul id yang sama. Hal ini menunjukkan bahwa variable x maupun y memiliki id
referensi yang sama karena niali pada varibel x maupun y adalah sama-sama sebuah
onjek yang bernilai 9.

![enter image description here](https://i.ibb.co/PjBdhmS/9.png)

Berdasarkan potongan kode yang telah anda buat sebelumnya yang memiliki id yang
sama. Jika anda menggunakan perintah del untuk menghapus variable y, maka yang
akan dihapus adalah referensinya saja, bukan objek ‘9’ yang tadi ditunjuk oleh variable x
dan y. Eksekusi program seperti dibawah ini

![enter image description here](https://i.ibb.co/qM6L483/10.png)

Berdasarkan kode yang telah dibuat tambahkan kode seperti dibawah ini

![enter image description here](https://i.ibb.co/zSJLBDf/14.png)

Dengan menambahkan kode baris di atas, maka referensi objek varibel x akan
dipindahkan dari objek ‘9’ ke objek ‘True’. Dengan demikian objek lama (9) akan diklaim
sebagai sampah karena objek tersebut tidak ditunjuk oleh variable apapun.

## Membuat Kode Program

1. Buat direktori tempat penyimpanan anda
2. Jalankan program teks editor Pycharm
3. Tuliskan kode sebagai berikut
4. Simpan file tersebut dengan nama hello.py

![enter image description here](https://i.ibb.co/Zc7cmh2/15.png)

## Python Bersifat Case Sensitive
Penulisan kode program pada pythonbersifat case sensitive. Dengan demikian misal
variable Posisi akan berbeda dengan variable posisi. Coba eksekusilan program
berikut

![enter image description here](https://i.ibb.co/B2ZLW2g/16.png)

## Perintah Program (Statement)

Pada python stiap kode program yang dituliskan tidak harus diakhiri dengan sebuah
statement (biasanya tanda titik koma) seperti pada Java dan C. Titik koma pada python
hanya diberikan pada saat ada dua atau lebih statement pada satu baris yang sama.
Tuliskan kode berikut pada computer.

![enter image description here](https://i.ibb.co/1dLv0qc/17.png)

Secara umum perintah program ditulis dalam satu baris kode, tetapi jika perintah yang
dituliskan panjang maka anda dapat memecah perintah tersebut menjadi beberapa baris.
Dimana setiap baris harus dihubungkan dengan tanda backslash (\). Coba tuliskan
program berikut pada computer.

![enter image description here](https://i.ibb.co/8MM3pyV/18.png)

Tetapi tanda backslah tidak diperlukan jika kita menulis perintah kode dalam bentuk
array atau kode yang terdapat diantara tanda (…), […] atau {…}. Tuliskan kode berikut
pada computer.

![enter image description here](https://i.ibb.co/NprT7W1/19.png)

## Tipe Numerik
### Bilangan Bulat

Dalam python terapat dua tipe bilangan bulat yaitu int dan bool. Selain tipe integral
primitive python juga dapat menggunakan bilangan integral dengan basis decimal
(10), biner (2), octal (8) maupun heksadesimal (16). Tuliskan kode program berikut
pada computer.

![enter image description here](https://i.ibb.co/tCn1XRc/20.png)

Tipe bilangan bulat yang kedua adalah tipe Boolean, dimana seperti yang telah kita
ketahui tipe data boleean bernilai true atau false saja. Tuliskan kode program berikut
pada computer.

![enter image description here](https://i.ibb.co/d7ttZHK/21.png)

Proses perhitungan dan penambahan bilangan pada python akan menghasilkan objek
baru, hal ini terlihat dari id nya.

![enter image description here](https://i.ibb.co/jH2rvp1/23.png)

### Bilangan Riil

Untuk tipe bilangan riil, python menyediakan tipe float, decimal.Decimal dan
complex. Type bilangan float menggunakan titik untuk tanda desimalnya.

![enter image description here]("https://i.ibb.co/7tDSNJz/24.png)

Sedangkan untuk tipe decimal hampir sama dengan tipe data float, akan ntetapi tipe
decimal digunakn untuk melakukan perhitungan dengan nilai koma yang lebih
presisi.

## Tipe String

Tipe data string dalam python direpresentasikan dengan tipe str. Objek string dapat
dibuat dengan tiga cara yaitu:
• Menggunakan tanda pertik tunggal
• Menggunakan tanda petik ganda
• Menggunakan tanda petik tunggal ataupun ganda yang direpetisi sebanyak tiga kali

![enter image description here]("https://i.ibb.co/Bq3C10n/25.png)

Objek dalam string tidak dapat dirubah, tiap karakter di dalam string dapat diakses
dengan tanda [] diikuti nomor array-nya. Berdasarkan variable yang telah anda buat
sebelumnya buatlah kode program berikut, apa hasilnya?, lakukan dengan variable yang
lainnya

![enter image description here](https://i.ibb.co/GkCPJ7j/26.png)

dalam string kita dapat memberikan kareakter khusus antara lain \n untuk memberikan
enter, \’ untuk membnerikan petik tunggal, \t untuk memberikan tab. Pada dasarnya 
karakter khusus dalam phyton harus diawali dengan backslash (\) diikuti dengan
karakter khususnya.

![enter image description here](https://i.ibb.co/DkGnWbp/27.png)

Python juga dapat menggabungkan dua objek string menjadi satu dengan operator +.
Dengan kode yang telah di tuliskan sebelumnya gabungkan dengan string berikut dan
lihat hasilnya

![enter image description here](https://i.ibb.co/fM8j6Jz/28.png)

### Membandingkan String
Untuk membandingkan kesamaan string python menggunakan operator ==.
Sedangkan untuk membandingkan id objek string menggunakan is. Selain kedua
operator tersebut, python juga dapat menggunakan operator lainnya untuk
membandingkan tipe data string. Tuliskan kode program berikut dan gumakan
operator >, <=, >=, apa yang dihasilkan?

![enter image description here](https://i.ibb.co/r5PJKZf/29.png)

### Mengekstrak Substring
Substring di dalam string dapat diekstrak dengan menggunakan operator slice (:)
dengan menyertakan indeks awal dan akhir sebagai penanda. Tuliskan kode program
dibawah ini.

![enter image description here](https://i.ibb.co/phhF1Jr/30.png)

Kode tersebut mengambil substring dari variable s mulai dari indeks ke 0 sampai
indeks ke 11. Jika kita tidak menyertakan indeks maka string yang akan diekstrak
adalah sepanjang string tersebut / string sisanya. Tuliskan kode program berikut.

![enter image description here](https://i.ibb.co/DRyyH8R/31.png)

### Membuat String Dengan Format Tertentu
Phyton pada dasarnya juga dapat memnggabungkan tipoe data atau format lain ke
dalam string yang telah dibuat. Antara lain dengan menggunakan $d, %f, %s dan lain
sebagainya. Tuliskan kode program berikut.

![enter image description here](img src="https://i.ibb.co/QNF66hZ/32.png)

## Tipe Koleksi
Objek list dibuat dengan menggunakan tanda [], setiap objek yang berada di dlamnya
dipisahkan dengan menggunakan koma dan dapat terdiri dari berbagai macam tipe
data.

![enter image description here](https://i.ibb.co/WxSyyjz/33.png)

Model dan cara akses list dapat digabungkan dengan fungsi perulangan dasar seperti
for, while dan lain sebagainya.

![enter image description here](

Untuk menghapus atau merubah elemen pada list anda dapat menggunakan perintah
del[‘indeks_list’] sedangkan untuk merubah dapat menggunakan perintah
namaList[‘indeks’] = value baru. Untuk menambahkan elemen pada list anda dapat
menggunakan perintah extend([list])’.

![enter image description here](https://i.ibb.co/P17Q0Yc/34.png)
