import numpy as np
import matplotlib.pyplot as plt

def konvolusiX (im, kernel):
    h, w = im.shape
    hk = kernel.shape

    imhasil = np.zeros((h,w))
    offset = int(hk[0]/2)
    for i in range(offset, h-offset):
        for j in range(0,w):
            #hasil = kernel * im[i-1:i+2]
            hasil = kernel[0] * im[i-1,j] + kernel[1] * im[i,j] + kernel[2] * im[i+1,j]
            imhasil[i,j] = hasil
        
    return (imhasil)

def konvolusiX_1_abs(im, kernel):
    h, w = im.shape
    hk = kernel.shape

    imhasil = np.zeros((h,w))
    offset = int(hk[0]/2)
    for i in range(offset, h-offset):
        for j in range(0,w):
            #hasil = kernel * im[i-1:i+2]
            hasil = kernel[0] * im[i-1,j] + kernel[1] * im[i,j] + kernel[2] * im[i+1,j]
            imhasil[i,j] = abs(hasil)
        
    return (imhasil)

def konvolusiX_2_abs (im, kernel):
    h, w = im.shape
    hk = kernel.shape

    imhasil = np.zeros((h,w))
    offset = int(hk[0]/2)
    for i in range(offset, h-offset):
        for j in range(0,w - offset):
            #hasil = kernel * im[i-1:i+2]
            hasilX = kernel[0] * im[i-1,j] + kernel[1] * im[i,j] + kernel[2] * im[i+1,j]
            hasilY = kernel[0] * im[i,j-1] + kernel[1] * im[i,j] + kernel[2] * im[i,j+1]
            #imhasil[i,j] = hasil
            #imhasil[i,j] = abs(hasil)
            imhasil[i,j] = abs(hasilX + hasilY)
        
    return (imhasil)

def RUN():
    kernel = np.array([-1,0,1])
    im = plt.imread("kotak.jpg")
    imgray = 0.33*im[:,:,0] + 0.59*im[:,:,1] + 0.07*im[:,:,2]
    fdx = konvolusiX(imgray, kernel)
    fdx2 = konvolusiX_1_abs(imgray, kernel)
    fdx3 = konvolusiX_2_abs(imgray, kernel)

    plt.subplot(231)
    plt.imshow(im)
    plt.title("Gambar Warna")

    plt.subplot(232)
    plt.imshow(imgray, cmap='gray')
    plt.title("Gray")

    plt.subplot(233)
    plt.imshow(fdx, cmap="gray")
    plt.title("Dx")

    plt.subplot(234)
    plt.imshow(fdx2, cmap="gray")
    plt.title("Dx 2")

    plt.subplot(235)
    plt.imshow(fdx3, cmap="gray")
    plt.title("Dx 3")

    plt.show()

if __name__ == "__main__":
    RUN()