import numpy as np
import matplotlib.pyplot as plt

#ekstrak citra menjadi per elemen warna
def rgb(im):
    img = im.copy()
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]
    return(r, g, b)

def yuv(im):
    img = im.copy()
    w,h = im.shape()
    valYuv = [[0.299, 0.587, 0.114],[-0.169, -0.331, 0.500],[0.500, -0.419, -0.081]]
    r, g, b = rgb(im)
    print(r[5,1],"\n", g[2,5],"\n", b[4,10])

    for i in range(h):
        for j in range(w):
            valRGB = [r[i,j], g[i,j], b[i,j]]
            val = np.matmul(valYuv, valRGB)
        return(val)
    
    plt.subplot(222)
    plt.imshow(val[0])
    plt.subplot(223)
    plt.imshow(val[1])
    plt.subplot(224)
    plt.imshow(val[2])

    return(y, u, v)

def RUN():
    #baca citra
    im = plt.imread('bunga.jpg')
    #c_h = hsi(im)

    plt.subplot(221)
    plt.imshow(rgb(im))

    yuv(im)
    plt.show()

if __name__ == "__main__":
    RUN()