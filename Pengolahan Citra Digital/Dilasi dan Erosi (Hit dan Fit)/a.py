import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(im):
    gray = 0.23*im[:,:,0] + 0.77*im[:,:,1] + 0.11*im[:,:,2]
    return(gray)

def gray2biner(imgray):
    biner = np.where(imgray >140, 255, 0)/255
    return(biner)

def dilasi(imbiner):
    #proses
    se = np.array([[1,1,1],[1,1,1],[1,1,1]])
    h, w = imbiner.shape
    imhit = np.zeros((h, w))
    for i in range (1, h-1):
        for j in range (1, w-1):
            hasil = imbiner[i-1:i+2,j-1:j+2]*se
            if np.sum(hasil)>=1:
                imhit[i, j] = 1
    return (imhit)


def erosi(imbiner):
    se = np.array([[1,1,1],[1,1,1],[1,1,1]])
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
    im = plt.imread("buah.jpg")
    im_asli = im.copy()
    imop = im.copy()

    #konversi ke gray
    imgray = rgb2gray(im)

    #konversi ke biner
    biner = gray2biner(imgray)

    #show image
    plt.subplot(251)
    plt.title("asli")
    plt.imshow(im_asli)

    plt.subplot(252)
    plt.title("biner")
    plt.imshow(biner, cmap = 'gray')

    plt.subplot(253)
    plt.title("erosi")
    plt.imshow(erosi(biner), cmap = "gray")
 
    plt.subplot(254)
    plt.title("dilasi")
    plt.imshow(dilasi(biner), cmap='gray')

    plt.subplot(255)
    imop[:,:,0] = dilasi(biner) * im[:,:,0]
    imop[:,:,1] = dilasi(biner) * im[:,:,1]
    imop[:,:,2] = dilasi(biner) * im[:,:,2]
    plt.title("dilasi to rgb")
    plt.imshow(imop, cmap = "gray")

    plt.subplot(256)
    imop[:,:,0] = erosi(biner) * im[:,:,0]
    imop[:,:,1] = erosi(biner) * im[:,:,1]
    imop[:,:,2] = erosi(biner) * im[:,:,2]
    plt.title("erosi to rgb")
    plt.imshow(imop, cmap = "gray")

    #opening
    plt.subplot(257)
    opening = dilasi(erosi(biner))
    plt.title("opening")
    plt.imshow(opening, cmap = "gray")

    #closing
    plt.subplot(258)
    closing = erosi(dilasi(biner))
    plt.title("closing")
    plt.imshow(closing, cmap = "gray")

    plt.subplot(259)
    imop[:,:,0] = opening * im[:,:,0]
    imop[:,:,1] = opening * im[:,:,1]
    imop[:,:,2] = opening * im[:,:,2]
    plt.title("opening to rgb")
    plt.imshow(imop, cmap = "gray")

    plt.subplot(2,5,10)
    imop[:,:,0] = closing * im[:,:,0]
    imop[:,:,1] = closing * im[:,:,1]
    imop[:,:,2] = closing * im[:,:,2]
    plt.title("closing to rgb")
    plt.imshow(imop, cmap = "gray")

    plt.show()

if __name__ == "__main__":
    main()



