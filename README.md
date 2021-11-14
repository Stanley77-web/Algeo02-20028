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
***[Setup hanya disediakan untuk Sistem Operasi Windows]***
1. Download dan install [python3](https://www.python.org/downloads/)
2. Clone repository ini menggunakan perintah berikut (git bash):
```
$ git clone https://github.com/Stanley77-web/Algeo02-20028.git
```
3. Buka terminal command prompt, kemudian arahkan direktori terminal tersebut pada folder repository
    
    ![image](https://user-images.githubusercontent.com/73146752/141693306-29b73c48-1ad1-4b1d-a9b8-b2bad00716f8.png)
    
    ![image](https://user-images.githubusercontent.com/73146752/141693385-7c7f821f-dc3c-4cb1-9952-a4b46b470d92.png)

4. Arahkan direktori pada folder *api* terminal dengan menuliskan perintah:
```
$ cd src\react-flask-app\api
```
   ![image](https://user-images.githubusercontent.com/73146752/141691187-2540e143-b887-4343-a2bf-eaef7ea48b26.png)
   
5. Buatlah *virtual environment* dengan menuliskan perintah:
```
$ python3 -m venv venv
```

6. Kemudian, aktivasi *Scripts virtual environment* dengan menuliskan perintah berikut:
```
$ venv\Scripts\activate
```

7. *Install* semua library dengan menjalankan perintah-perintah berikut:
```
$ npm install
$ pip install flask python-dotenv
$ pip install pillow
$ pip install numpy
$ pip install Flask-Cors
```
8. Setelah meng-*install* semua *library*, siapkan dua buah terminal Powershell untuk menjalankan website dengan direktori yang sama pada nomor *4*.
9. Untuk menjalankan api, terminal Powershell pertama dituliskan perintah:
```
$ yarn start-api
```
10. Untuk menjalankan website, terminal Powershell kedua dituliskan perintah:
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
