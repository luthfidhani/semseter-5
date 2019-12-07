import numpy as np
import matplotlib.pyplot as plt
import math

#ekstrak citra menjadi per elemen warna
def rgb(im):
    img = im.copy()
    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]
    return(r, g, b)

def hsi(im):
    r, g, b = rgb(im)

    teta = math.acos((0.5 * (r - g) + (r - b))/(((r - g)**2 + (r - b)*(g - b))**0.5))
    s = 1 - (3/(r + g + b)) * np.min(r, g, b)
    i = 1/3 * (r + g + b)

    if b > g:
        h = 360 - teta
    elif b <= b:
        h=0
    print(h,"\n")
    print(s,"\n")
    print(i,"\n")
    return(h, s, i)

def RUN():
    #baca citra
    im = plt.imread('bunga.jpg')
    #c_h = hsi(im)

    plt.subplot(221)
    plt.imshow(im)

    hsi(im)
    plt.show()

if __name__ == "__main__":
    RUN()