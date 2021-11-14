# Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri
> Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Author](#author)
<!-- * [License](#license) -->

## General Information
Membuat program kompresi gambar dengan memanfaatkan algoritma SVD dalam bentuk 
website lokal sederhana. <br /> <br />
Spesifikasi website adalah sebagai berikut: 
- Website mampu menerima file gambar beserta input tingkat kompresi gambar 
(dibebaskan formatnya).
- Website mampu menampilkan gambar input, output, runtime algoritma, dan persentase 
hasil kompresi gambar (perubahan jumlah pixel gambar).
- File output hasil kompresi dapat diunduh melalui website.
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- [Python - version 3.8.5](https://en.wikipedia.org/wiki/Python_(programming_language)) 
- [React - version 17.0.2](https://en.wikipedia.org/wiki/React_(JavaScript_library)) 
- [Flask - version 2.0.2](https://en.wikipedia.org/wiki/Flask_(web_framework)) 

## Screenshots
![Example screenshot](./img/screenshot.png)
<!-- If you have screenshots you'd like to share, include them here. -->


## Setup
1. Download dan install [python3](https://www.python.org/downloads/)
2. Clone repository ini menggunakan perintah berikut (git bash):
```
$ git clone https://github.com/Stanley77-web/Algeo02-20028.git
```
3. Arahkan direktori ke dalam folder repository, lalu `Shift + Right Mouse Button` pada direktori kemudian pilih opsi `Open Powershell Window here`
![Terminal](https://user-images.githubusercontent.com/73146752/141690744-807b7a57-f580-47f3-9e2e-8082f202b0f1.png)
4. Setelah terminal Powershell terbuka, buat virtual environment dengan menuliskan command:
```
$ python3 -m venv venv
```
5. Kemudian, aktivasi Scripts virtual environment dengan menuliskan perintah berikut:
```
$ venv\Scripts\activate
```

6. *Install* semua library dengan menjalankan perintah-perintah berikut:
```
$ npm install
$ pip install flask python-dotenv
$ pip install pillow
$ pip install numpy
$ pip install Flask-Cors
```
7. Setelah meng-install semua library, siapkan dua buah terminal untuk menjalankan website.
8. Terminal pertama dijalankan perintah:
```
$ yarn start-api
```
9. Terminal kedua dijalankan perintah:
```
$ yarn start
```

## Author
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
