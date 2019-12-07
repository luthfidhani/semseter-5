import numpy as np
import matplotlib.pyplot as plt

def histogram(im):
    w, h = im.shape
    histo = np.zeros(256)

    for i in range(w):
        for j in  range(h):
            histo[im[i,j]] += 1
    return(histo)

def im_gray(im):
    img = im.copy()
    imgray = np.int16(0.21*img[:,:,0] + 0.71*img[:,:,1] + 0.07*img[:,:,2])
    imgray[imgray>255] = 255
    return(imgray)


def RUN():
    #baca image
    #im = plt.imread('bunga.jpg')
    im = plt.imread('a.jpg')
    gray = im_gray(im)
    #nhisto = np.int16(histogram(gray))
    #print(nhisto)
    #plt.hist(gray, bins=10)
    #plt.show()

    histo1 = im.mean(axis=2).flatten()
    print("Dimensi Histo : ", histo1.shape)
    b, ins, patch = plt.hist(histo1, 255)
    plt.xlim([0,255])
    plt.show()



if __name__ == "__main__":
    RUN()