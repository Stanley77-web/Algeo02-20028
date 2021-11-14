import numpy as np
import numpy.linalg
from PIL import Image
import sys
import os


def CompressChannel(channelMatrix, k, eigen_total):
    """ 
    Menghasilkan matriks hasil kompresi menggunakan algoritma SVD.
    """
    U, S, VT = SVD(channelMatrix, eigen_total)
    A = U[:, 0:k] @ S[0:k, 0:k] @ VT[0:k, :]
    compressed = np.clip(A, 0, 255).astype('uint8')
    return compressed


def SVD(matrix, k):
    """
    Menghasilkan komponen SVD dengan menggunakan konsep power iteration serta konsep perkalian matriks invers.
    """
    # KAMUS LOKAL
    baris, kolom = matrix.shape  # baris dan kolom matriks

    # ALGORITMA
    if(baris <= kolom):
        A = matrix @ matrix.T
        n = baris
    elif(baris > kolom):
        A = matrix.T @ matrix
        n = kolom
    # Algoritma QR
    Q = np.random.rand(n, k)
    Q, _ = np.linalg.qr(Q)
    # Skema power iteration
    for i in range(150):
        Z = A.dot(Q)
        Q, R = np.linalg.qr(Z)
    # Semua nilai singular values
    diag = np.sqrt(np.abs(np.diag(R)))
    # Mengubah nilai singular values agar memiliki invers
    for i in range(diag.shape[0]):
        if diag[i] < 1:
            diag[i] = 0.1
    S = np.diag(diag)
    # Skema perkalian matriks invers untuk mendapatkan semua komponen
    if(baris <= kolom):
        U = Q
        US = U @ S
        inv = np.linalg.inv(US)
        VT = inv @ matrix
    elif(baris > kolom):
        VT = Q.T
        SVT = S @ VT
        inv = np.linalg.inv(SVT)
        U = matrix @ inv
    return U, S, VT


# PROGRAM UTAMA
def mainCompress():
    # ALGORITMA
    file = str(input())
    ratio = float(input())
    sys_path = sys.path[0]
    load_path = "../../test/testgambar/" + file
    path = os.path.join(sys_path, load_path)
    pic = Image.open(path)

    # Mengecek jenis gambar
    if pic.mode == "RGBA":
        alpha = pic.getchannel('A')
    elif len(pic.getbands()) == 1:
        pic = pic.convert("RGBA")
        alpha = pic.getchannel('A')

    # Ukuran width dan height gambar
    pixel = np.array(pic)
    width = pixel.shape[0]
    height = pixel.shape[1]
    # Tingkat kompresi gambar
    total_k = min(height, width)
    new_ratio = 100 - ratio
    k = round(total_k * new_ratio / 100)

    # Konversi channel gambar menjadi matriks
    red = np.asarray(pic.getchannel('R')).astype(float)
    green = np.asarray(pic.getchannel('G')).astype(float)
    blue = np.asarray(pic.getchannel('B')).astype(float)
    # Kompresi matriks channel
    redCompressed = CompressChannel(red, k, total_k)
    greenCompressed = CompressChannel(green, k, total_k)
    blueCompressed = CompressChannel(blue, k, total_k)
    # Konversi matriks menjadi channel gambar
    redImage = Image.fromarray(redCompressed)
    blueImage = Image.fromarray(blueCompressed)
    greenImage = Image.fromarray(greenCompressed)

    # Membuat gambar berdasarkan format
    if alpha:
        newImage = Image.merge(
            "RGBA", (redImage, greenImage, blueImage, alpha))
    else:
        newImage = Image.merge("RGB", (redImage, greenImage, blueImage))
    save_path = "../../test/testgambar/" + "compressed_" + file
    path = os.path.join(sys_path, save_path)
    newImage.save(path)


# Menjalankan Program
mainCompress()
