import numpy as np
import matplotlib.pyplot as plt

def Red(im):
    img = im.copy()
    img[:,:,1] = 0
    img[:,:,2] = 0
    return(img)

def Green(im):
    img = im.copy()
    img[:,:,0] = 0
    img[:,:,2] = 0
    return(img)

def Blue(im):
    img = im.copy()
    img[:,:,0] = 0
    img[:,:,1] = 0
    return(img)

def Grey(im):
    img = im.copy()
    img_gray = np.int16(0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.11*img[:,:,2])
    return(img_gray)

def run():
    #baca citra
    im = plt.imread('bunga.jpg')

    #tampil merah
    plt.subplot(221)
    plt.imshow(Red(im))
    
    #tampil Green
    plt.subplot(222)
    plt.imshow(Green(im))

    #tampil Blue
    plt.subplot(223)
    plt.imshow(Blue(im))

    #tampil Grey
    plt.subplot(224)
    plt.imshow(Grey(im), cmap='gray')

    plt.show()

   baris400 = Red[100:101,0:300,0]
   print(baris400)

if __name__ == '__main__':
    run()