# Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri
> Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar

## Daftar Isi
* [Informasi Umum](#informasi-umum)
* [Teknologi Digunakan](#teknologi-digunakan)
* [Screenshots](#tampilan-website)
* [Setup](#setup)
* [Penulis](#penulis)
<!-- * [License](#license) -->

## Informasi Umum
Membuat program kompresi gambar dengan memanfaatkan algoritma SVD dalam bentuk 
website lokal sederhana. <br /> <br />
Spesifikasi website adalah sebagai berikut: 
- Website mampu menerima file gambar beserta input tingkat kompresi gambar 
(dibebaskan formatnya).
- Website mampu menampilkan gambar input, output, runtime algoritma, dan persentase 
hasil kompresi gambar (perubahan jumlah pixel gambar).
- File output hasil kompresi dapat diunduh melalui website.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Teknologi Digunakan
- [Python - version 3.8.5](https://en.wikipedia.org/wiki/Python_(programming_language)) 
- [React - version 17.0.2](https://en.wikipedia.org/wiki/React_(JavaScript_library)) 
- [Flask - version 2.0.2](https://en.wikipedia.org/wiki/Flask_(web_framework)) 

## Tampilan Website

![image](https://user-images.githubusercontent.com/73146752/141695778-f849f46f-312f-4a04-970b-e56c1fbaba2a.png)

## Setup
***[Setup hanya disediakan untuk Sistem Operasi Windows]***
1. Download dan install [python3](https://www.python.org/downloads/)
2. Clone repository ini menggunakan perintah berikut (git bash):
```
$ git clone https://github.com/Stanley77-web/Algeo02-20028.git
```
3. Buka terminal Command Prompt, kemudian arahkan direktori terminal pada folder repository seperti gambar berikut:

   ![image](https://user-images.githubusercontent.com/73146752/141693651-37b17ad6-8d50-407a-8182-12a3196a065b.png)
    
   ![image](https://user-images.githubusercontent.com/73146752/141693306-29b73c48-1ad1-4b1d-a9b8-b2bad00716f8.png)
    
4. Buatlah *virtual environment* dengan menuliskan perintah:
```
$ python3 -m venv venv
```

5. Kemudian, aktivasi *Scripts* dari *virtual environment* dengan menuliskan perintah:
```
$ venv\Scripts\activate
```
   ![image](https://user-images.githubusercontent.com/73146752/141694110-cb2b45a8-f3b3-4c43-8c1c-f1854cc452ea.png)

6. *Install* semua *library* dengan menjalankan perintah-perintah berikut:
```
$ npm install
$ pip install flask python-dotenv
$ pip install pillow
$ pip install numpy
$ pip install Flask-Cors
```

7. Setelah meng-*install* semua *library*, siapkan dua buah terminal Command Prompt dengan direktori dan aktivasi *Virtual Environment* yang sama dengan langkah *5*.
8. Terminal Command Prompt pertama dituliskan perintah:
```
$ yarn start-api
```
   ![image](https://user-images.githubusercontent.com/73146752/141695513-91770eef-c6d7-4323-8517-eac7dad3b008.png)
   
9. Terminal Command Prompt kedua dituliskan perintah:
```
$ yarn start
```
Terminal akan menampilkan URL website dari program. Salin URL tersebut dan buka pada browser yang ingin dipakai, Selamat Mencoba!
    
   ![image](https://user-images.githubusercontent.com/73146752/141695854-50e7fc33-349e-4e77-96c3-990b93ae8b0b.png)
    
## Penulis
<table>
    <tr>
      <td><b>Nama</b></td>
      <td><b>NIM</b></td>
    </tr>
    <tr>
      <td><b>Timothy Stanley Setiawan</b></td>
      <td><b>13520028</b></td>
    </tr>
    <tr>
      <td><b>Farrel Farandieka Fibriyanto</b></td>
      <td><b>13520054</b></td>
    </tr>
    <tr>
      <td><b>Jeremy Rionaldo Pasaribu</b></td>
      <td><b>13520082</b></td>
    </tr>
</table>
