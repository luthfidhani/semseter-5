import numpy as np
import matplotlib.pyplot as plt

def konvolusi (imgray, kmask):
    w, h = imgray.shape
    wk, hk = kmask.shape
    offset = int(wk/2)

    imhasil = np.zeros((w,h))
    for i in range(offset, w-offset):
        for j in range(offset, h - offset):
            hasil = np.sum(kmask * imgray[i-offset:i+offset+1, j-offset:j+offset+1])
            imhasil[i,j] = abs(hasil)
    return (imhasil)


def RUN():
    im = plt.imread("ironman.jpg")
    im_gray = 0.33 * im[:,:,0] + 0.59 * im[:,:,1] + 0.07 * im[:,:,2]

    kernel = np.array([[0,0,0],[-1,0,1],[0,0,0]])
    Dx = konvolusi(im_gray, kernel)
    #Dx = np.where(Dx > 20, 1, 0) #(coba dibuka komennya, dan cari perbedannya)

    kernelX = np.array([[0,0,0],[-1,0,1],[0,0,0]])
    DxX = konvolusi(im_gray, kernelX)
    

    kernelY = np.array([[0,-1,0],[0,0,0],[0,1,0]])
    DxY = konvolusi(im_gray, kernelY)
    DF = DxX + DxY

    DF = np.where(DF > 10, 1, 0) #(coba dibuka komennya, dan cari perbedannya)
    DxX = np.where(DxX > 10, 1, 0) #(coba dibuka komennya, dan cari perbedannya)
    DxY = np.where(DxY > 10, 1, 0) #(coba dibuka komennya, dan cari perbedannya)

    

    plt.subplot(231)
    plt.imshow(im)
    plt.title("Warna")

    plt.subplot(232)
    plt.imshow(im_gray, cmap="gray")
    plt.title("Gray")

    plt.subplot(233)
    plt.imshow(Dx, cmap="gray")
    plt.title("Dx")

    plt.subplot(234)
    plt.imshow(DxX, cmap="gray")
    plt.title("DxX")

    plt.subplot(235)
    plt.imshow(DxY, cmap="gray")
    plt.title("DxY")

    plt.subplot(236)
    plt.imshow(DF, cmap="gray")
    plt.title("DF")

    plt.show()


if __name__ == "__main__":
    RUN()