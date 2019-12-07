import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(im):
    gray = 0.23*im[:,:,0] + 0.77*im[:,:,1] + 0.11*im[:,:,2]
    return(gray)

def gray2biner(imgray):
    biner = np.where(imgray >140, 0, 255)/255
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
    im = plt.imread("anggur.jpg")
    im_asli = im.copy()
    imop = im.copy()

    #konversi ke gray
    imgray = rgb2gray(im)

    #konversi ke biner
    biner = gray2biner(imgray)

    #show image

    eros = erosi(dilasi(dilasi(dilasi(dilasi(biner)))))
    dilas = dilasi(dilasi(erosi(erosi(biner))))

    plt.subplot(221)
    plt.title("erosi")
    plt.imshow(eros, cmap = "gray")
 
    plt.subplot(222)
    plt.title("dilasi")
    plt.imshow(dilas, cmap='gray')

    plt.subplot(224)
    imop[:,:,0] = dilas * im[:,:,0]
    imop[:,:,1] = dilas * im[:,:,1]
    imop[:,:,2] = dilas * im[:,:,2]
    plt.title("dilasi to rgb")
    plt.imshow(imop, cmap = "gray")

    plt.subplot(223)
    imop[:,:,0] = dilasi(biner) * im[:,:,0]
    imop[:,:,1] = dilasi(biner) * im[:,:,1]
    imop[:,:,2] = dilasi(biner) * im[:,:,2]
    plt.title("dilasi to rgb")
    plt.imshow(imop, cmap = "gray")

    plt.show()

if __name__ == "__main__":
    main()



