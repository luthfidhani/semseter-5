import numpy as np
import matplotlib.pyplot as plt


#asumsi semua gambar adalah grey
def Grey(im):
    img = im.copy()
    img_gray = np.int16(0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.11*img[:,:,2])
    return(img_gray)

def negatif(img_gray):
    neg = 255 - img_gray
    return(neg)

def run():
    #baca citra
    im = plt.imread('C:/Users/Anonym0x/Documents/python/a.jpg')

    im_negatif = negatif(Grey(im))

    #show image
    plt.subplot(121)
    plt.imshow(Grey(im), cmap='gray')

    plt.subplot(122)
    plt.imshow(im_negatif, cmap='gray')
    plt.show()

if __name__ == '__main__':
    run()