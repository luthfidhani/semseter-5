import numpy as np
import matplotlib.pyplot as plt

def bin2dec(a):
	hasil =0
	for i in range(len(a)):
		hasil = hasil + a[i]*2**i
	return hasil

def lbp(sub_im):
	hasil= np.zeros(8)
	hasil[0] = 1 if sub_im[0,0] > sub_im[1,1] else 0
	hasil[1] = 1 if sub_im[0,1] > sub_im[1,1] else 0
	hasil[2] = 1 if sub_im[0,2] > sub_im[1,1] else 0
	hasil[3] = 1 if sub_im[1,2] > sub_im[1,1] else 0
	hasil[4] = 1 if sub_im[2,2] > sub_im[1,1] else 0
	hasil[5] = 1 if sub_im[2,1] > sub_im[1,1] else 0
	hasil[6] = 1 if sub_im[2,0] > sub_im[1,1] else 0
	hasil[7] = 1 if sub_im[1,0] > sub_im[1,1] else 0
	out_hasil =bin2dec(hasil)
	return (out_hasil)

def rgb2gray(im):
	hasil = 0.33*im[:,:,0]+ 0.59*im[:,:,1]+0.07*im[:,:,2]
	return (hasil)
	
def gray2lbp(im_gray):
	w,h = im_gray.shape
	hasil = np.zeros((w,h))
	for i in range(1,w-1):
		for j in range(1, h-1):
			hasil[i,j]= lbp(im_gray[i-1: i+2, j-1:j+2])
	return (hasil)


def RUN():
	im = plt.imread('pesawat.jpg')
	im_gray=rgb2gray(im)
	im_Lbp= gray2lbp(im_gray)
	plt.subplot(121);
	plt.imshow(im_gray,cmap='gray')
	plt.subplot(122);
	plt.imshow(im_Lbp,cmap='gray')
	plt.show()
	
if __name__=="__main__":
	RUN()