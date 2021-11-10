import numpy as np
import numpy.linalg
from PIL import Image
from datetime import datetime
import sys
import os


def CompressSVD(channelDataMatrix, k):
    U, S, VT = SVD(channelDataMatrix, channelDataMatrix.shape[0])
    A = U[:, 0:k] @ S[0:k, 0:k] @ VT[0:k, :]
    compressed = np.clip(A, 0, 255).astype('uint8')
    return compressed


def SVD(matrix, k):
    b, k = matrix.shape
    # Jika jumlah baris matrix < jumlah kolom matrix
    if(b <= k):
        A = matrix @ matrix.T
        n = b
    # Jika jumlah baris matrix > jumlah kolom matrix
    elif(b > k):
        A = matrix.T @ matrix
        n = k
    # Menggunakan skema simultaneous power iteration
    Q = np.random.rand(n, k)
    Q, _ = np.linalg.qr(Q)
    for i in range(200):
        Z = A.dot(Q)
        Q, R = np.linalg.qr(Z)
    # Mengambil nilai egeinvalue dari matriks R dengan terlebih dahulu
    #   membuat nilai matriks tersebut absolut agar tidak error lalu
    #   mengambil nilai diagonal matriks tersebut kemudian diakarkan
    diag = np.sqrt(np.abs(np.diag(R)))
    # Membuat nilai eigenvalue 0 menjadi 0.1 agar membuat
    #   matriks untuk memiliki invers
    for i in range(diag.shape[0]):
        if diag[i] < 1:
            diag[i] = 0.1
    S = np.diag(diag)  # Membuat matriks persegi dari nilai diagonal eigenvalue
    # Mendapatkan matriks singular kiri/kanan dengan persamaan invers
    #   tergantung pada ukuran matrix awal
    if(b <= k):
        U = Q
        US = U @ S
        inv = np.linalg.inv(US)
        VT = inv @ matrix
    elif(b > k):
        VT = Q.T
        SVT = S @ VT
        inv = np.linalg.inv(SVT)
        U = matrix @ inv
    return U, S, VT


# PROGRAM UTAMA
def mainCompress():
    startTime = datetime.now()
    file = str(input("Masukkan nama file: "))
    ratio = float(input("Masukkan rasio: "))
    # path = 'wat.png'
    # ratio = 5
    sys_path = sys.path[0]

    load_path = "../../test/testgambar/" + file
    path = os.path.join(sys_path, load_path)

    pic = Image.open(path).convert("RGBA")
    pixel = np.array(pic)
    imageWidth = pixel.shape[0]
    imageHeight = pixel.shape[1]
    red = np.asarray(pic.getchannel('R')).astype(float)
    green = np.asarray(pic.getchannel('G')).astype(float)
    blue = np.asarray(pic.getchannel('B')).astype(float)
    alpha = pic.getchannel('A')

    total_k = min(imageHeight, imageWidth)
    k = round(total_k * ratio / 100)

    redCompressed = CompressSVD(red, k)
    greenCompressed = CompressSVD(green, k)
    blueCompressed = CompressSVD(blue, k)
    redImage = Image.fromarray(redCompressed)
    blueImage = Image.fromarray(blueCompressed)
    greenImage = Image.fromarray(greenCompressed)

    newImage = Image.merge("RGBA", (redImage, greenImage, blueImage, alpha))
    save_path = "../../test/testgambar/" + "converted.png"
    path = os.path.join(sys_path, save_path)
    newImage.save(path)
    print("Besaran: " + str(round(ratio, 2)) + "% dari gambar original ")
    time = datetime.now() - startTime
    print(f"{time.total_seconds():.0f} Seconds")


# Menjalankan Program
mainCompress()
