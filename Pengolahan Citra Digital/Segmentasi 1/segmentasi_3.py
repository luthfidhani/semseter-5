import numpy as np
import matplotlib.pyplot as plt
#import scipy.signal.convolve as scon
import scipy.ndimage.filters as filter

def RUN():
    im = plt.imread("ironman.jpg")
    im_gray = 0.33 * im[:,:,0] + 0.59 * im[:,:,1] + 0.07 * im[:,:,2]

    kernel = np.array([[0,0,0],[-1,0,1],[0,0,0]])
    kernelX = np.array([[0,0,0],[-1,0,1],[0,0,0]])
    kernelY = np.array([[0,-1,0],[0,0,0],[0,1,0]])

    Dx = filter.convolve(im_gray, kernel)
    DxX = filter.convolve(im_gray,kernelX)
    DxY = filter.convolve(im_gray,kernelY)
    DF = DxX + DxY
    

    print("Nilai Max : ", np.max(Dx))
    print("Nilai Min : ", np.min(Dx))

    plt.subplot(231)
    plt.imshow(im)
    plt.title("Warna")

    plt.subplot(232)
    plt.imshow(im_gray, cmap="gray")
    plt.title("Gray")

    plt.subplot(233)
    plt.imshow(np.abs(Dx), cmap="gray")
    plt.title("Dx")

    # coba hilangkan np.abs() dan rasakan bedanya :D
    plt.subplot(234)
    plt.imshow(np.abs(DxX), cmap="gray")
    plt.title("DxX")

    plt.subplot(235)
    plt.imshow(np.abs(DxY), cmap="gray")
    plt.title("DxY")

    plt.subplot(236)
    plt.imshow(np.abs(DF), cmap="gray")
    plt.title("DF = DxX + DxY")

    plt.show()


if __name__ == "__main__":
    RUN()