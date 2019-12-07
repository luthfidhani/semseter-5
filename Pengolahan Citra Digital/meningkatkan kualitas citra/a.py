import numpy as np
import matplotlib.pyplot as plt

def im_enhance(im):
    img =im.copy()
    h , w , d=im.shape
    for i in range(h):
        for j in range(w):
            img[i,j,0] +=50
            img[i,j,1] +=50
            img[i,j,2] +=50
            
            if img[i,j,0] >= 255:
                img[i,j,0] = 255
                
            if img[i,j,1] >= 255:
                img[i,j,1] = 255
                
            if img[i,j,2] >= 255:
                img[i,j,2] = 255
                
    return(img)
    
def im_enhance2(im):
    img =im.copy()
    img = np.int16(img+50)
    img[img>=255] = 255
    return (img)

def im_negative(im):
    img =im.copy()
    img = 256-1-img
    return (img)

def im_gray(im):
    im_gray=(im[:,:,0]*0.21+im[:,:,1]*0.71+im[:,:,2]*0.7)/255
    return (im_gray)

def im_logtrans(im):
    img = im.copy()
    #asumsi c = 1
    c = 0.2
    img = c*np.log(1+img)
    img[img>255] = 255
    return(img)

def im_powerlawtrans(im):
    img = im.copy()
    c = 1
    g = 0.04
    #img = c * img ** g
    #img[img>255] = 255
    img = np.int16(c *(img ** g))
    img[img>1.0] = 1.0
    return(img)

def im_peacetrans(im):
    img = im.copy() / 255
    ty1 = 0.0
    ty2 = 170 / 255
    ty3 = 200 / 255

    tx1 = 0.0
    tx2 = 50 / 255
    tx3 = 210 / 255

    h, w = im.shape
    im_proces = np.zeros((h,w))
    
    for i in range(h):
        for j in range(w):
            if(img[i,j] < tx2):
                im_proces[i,j] = (170/50) * img[i,j]
            elif (img[i,j]> tx3):
                im_proces[i,j] = (3/16) * (img[i,j] - tx2) + ty2
            else:
                im_proces[i,j] = (11/9) * (img[i,j] - tx3) + ty3
    return(im_proces)

    img[img<tx2] = (170/50) * img
    img = np.where(img<tx3, (3/16)*(img-tx2)+ty2, (11/9)*(img-tx3)+ty3)

    return(img)
    
def RUN():
    im =plt.imread('a.jpg')
    plt.subplot(121)
    plt.imshow(im, cmap='gray')
    
    plt.subplot(122)
    plt.imshow(im_peacetrans(im), cmap='gray')
    
    plt.show()
    
if __name__ == '__main__':
        RUN()