import numpy as np
import matplotlib.pyplot as plt

#asumsi image berwarna
def im_enhance(im):
    img = im.copy()
    h, w, d = im.shape
    for i in range(h):
        for j in range(w):
            img[i,j,0] += 50 #red
            img[i,j,1] += 50 #green
            img[i,j,2] += 50 #blue

            if img[i,j,0] >255:
                img[i,j,0] = 255

            if img[i,j,1] >255:
                img[i,j,1] = 255

            if img[i,j,2] >255:
                img[i,j,2] = 255
    return(img)

def im_enhance1(im):
    img = im.copy()
    img = np.int16(img)+50
    #img = np.where(img>255, 255, 0)
    img[img>=255] = 255

def im_negative(im):
    img = im.copy()
    img = 255 - img
    return(img)

def im_gray(im):
    imgray = np.int16(im[:,:,0]*0.21 + im[:,:,1]*0.71 + im[:,:,2]*0.71)
    return(imgray)

def im_logtrans(im):
    img = im.copy()
    #asumsi c = 1
    c = 0.2
    img = np.int16(c*np.log(1+img))
    img[img>255] = 255
    return(img)

def im_powerlawtrans(im):
    img = im.copy()
    c = 1
    g = 0.04
    img = c * np.power(img, g)
    img[img>255] = 255

    return(img)

def RUN():
    #baca citra
    im = plt.imread('a.jpg')
    plt.subplot(121)
    plt.imshow(im, cmap='gray')

    plt.subplot(122)
    #plt.imshow(im_enhance(im))
    #plt.imshow(im_negative(im))
    #plt.imshow(im_logtrans(im), cmap="gray")
    plt.imshow(im_powerlawtrans(im), cmap="gray")

    plt.show()

if __name__ == "__main__":
    RUN()