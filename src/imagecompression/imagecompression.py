import numpy as np
from PIL import Image
from SVDtest import *


def RealcompressSVD(channelDataMatrix, k):
    U, S, VT = np.linalg.svd(channelDataMatrix)
    S = np.diag(S)
    A = U[:, 0:k] @ S[0:k, 0:k] @ VT[0:k, :]
    compressed = A.astype('uint8')
    return compressed


def CompressSVD(channelDataMatrix, k):
    #U, S, VT = np.linalg.svd(channelDataMatrix)
    U, S, VT = SVD(channelDataMatrix, k)
    S = np.diag(S)
    A = U[:, 0:k] @ S[0:k, 0:k] @ VT[0:k, :]
    compressed = A.astype('uint8')
    # print(A)
    # print(compressed)
    np.savetxt('SVD_afterU.txt', U, fmt='%.5f')
    np.savetxt('SVD_after.txt', S, fmt='%.5f')
    return compressed


# PROGRAM UTAMA
# path = str(input("Masukkan nama file: "))
# ratio = float(input("Masukkan rasio: "))
startTime = datetime.now()
path = 'lena.png'
ratio = 50
pic = Image.open(path)
pixel = np.array(pic)
imageWidth = pixel.shape[0]
imageHeight = pixel.shape[1]
Red = pixel[:, :, 0]
Green = pixel[:, :, 1]
Blue = pixel[:, :, 2]

# image width and height:
print(imageWidth)
print(imageHeight)

# number of singular values to use for reconstructing the compressed image
k = round(imageWidth * ratio / 100)
print(k)

redCompressed = CompressSVD(Red, k)
# greenCompressed = CompressSVD(Green, k)
# blueCompressed = CompressSVD(Blue, k)
greenCompressed = RealcompressSVD(Green, k)
blueCompressed = RealcompressSVD(Blue, k)

redImage = Image.fromarray(redCompressed)
blueImage = Image.fromarray(blueCompressed)
greenImage = Image.fromarray(greenCompressed)

newImage = Image.merge("RGB", (redImage, greenImage, blueImage))
newImage.save('new.png')
print('Size:  ' +
      str(round(ratio, 2)) + '% of original image ')
print(datetime.now() - startTime)
