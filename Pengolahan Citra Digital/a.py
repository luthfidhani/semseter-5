import numpy as np
import matplotlib.pyplot as plt

im = plt.imread('C:/Users/Anonym0x/Documents/python/a.jpg')
h, w, d = im.shape
print("Height : ", h, "Width : ", w)

im_red = im.copy()
im_red[:,:,1] = 0 
im_red[:,:,2] = 0


baris400 = im_red[100:101,0:300,0]
#print(baris400.shape)

x = np.arange(baris400.shape[1])
y = x+2
print("x ", x)
print("baris400: ", baris400)

plt.subplot(211)
for y in baris400:
    plt.plot(x,y)

#plt.plot(baris400)

plt.subplot(212)

plt.imshow(im_red)
plt.show()