import numpy as np
import matplotlib.pyplot as plt

def red(im):

    im_red = im.copy()
    im_red[:,:,1] = 0 
    im_red[:,:,2] = 0

    return (im_red)

def rgb2gray(im):
    gray = 0.23*im[:,:,0] + 0.77*im[:,:,1] + 0.11*im[:,:,2]
    return(gray)

def gray2biner(imgray):
    biner = np.where(imgray >40, 255, 0)/255
    #biner = np.where(biner >=1, 1,0)
    return(biner)

def dilasi(imbiner):
    #proses
    ase = [1,0,1]
    se = np.array([ase, ase, ase])
    h, w = imbiner.shape
    imhit = np.zeros((h, w))
    for i in range (1, h-1):
        for j in range (1, w-1):
            hasil = imbiner[i-1:i+2,j-1:j+2]*se
            if np.sum(hasil)>=1:
                imhit[i, j] = 1
    return (imhit)

def erosi(imbiner):
    bse = [1,1,1]
    se = np.array([bse, bse, bse])
    h, w = imbiner.shape
    imhit = np.zeros((h, w))
    for i in range (1, h-1):
        for j in range (1, w-1):
            hasil = imbiner[i-1:i+2,j-1:j+2]*se
            if np.sum(hasil)==9:
                imhit[i, j] = 1
    return (imhit)

def main():
    #baca citra 
    im = plt.imread("koki.jpg")
    im_asli = im.copy()

    #ambil warna merah
    im_red = red(im)

    #konversi ke gray
    imgray = rgb2gray(im_red)

    #konversi ke biner
    biner = gray2biner(imgray)

    dilas = dilasi(biner)
    eros = erosi(biner)

    opening = dilasi(erosi(biner))
    closing = erosi(dilasi(biner))

    compound = opening + closing


    #show image
    plt.subplot(231)
    plt.title("asli")
    plt.imshow(im_asli)

    plt.subplot(232)
    plt.title("dilasi")
    plt.imshow(dilas, cmap='gray')

    plt.subplot(233)
    plt.title("erosi")
    plt.imshow(eros, cmap='gray')

    plt.subplot(234)
    plt.title("compound")
    plt.imshow(compound, cmap='gray')

    plt.subplot(235)
    plt.title("opening")
    plt.imshow(opening, cmap='gray')

    plt.subplot(236)
    plt.title("closing")
    plt.imshow(closing, cmap='gray')

    plt.show()

if __name__ == "__main__":
    main()



