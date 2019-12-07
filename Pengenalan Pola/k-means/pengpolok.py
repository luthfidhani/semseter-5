# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 12:48:32 2019

@author: Asus X550JX
"""

## Initialisation

#import xlrd as xl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'Iris.csv', index_col=0)

print(data.head())

f1=data['SepalLengthCm'].values
f2=data['SepalWidthCm'].values


print("==================================================")
print(f1)
print("==================================================")
print(f2)
print("==================================================")

X = np.array(list(zip(f1, f2)))

# Number of clusters
k = 3
# X coordinates of random centroids
C_x = np.random.randint(0, np.max(X), size=k)
# Y coordinates of random centroids
C_y = np.random.randint(0, np.max(X), size=k)


b1 = C_x
b2 = C_y

print("================ITERASI 0======================")
print("Centroid X dan Y")
print(b1)
print(b2)


jrk_f1=[]
i=0
j=0


for i in range(150):
    for j in range(3):
        c1 = np.sqrt(((f1[i]-b1[j])**2)+((f2[i]-b2[j])**2))
        jrk_f1.append(c1)
        
print("================")
print(jrk_f1)

def split(arr, size):
     arrs = []
     while len(arr) > size:
         pice = arr[:size]
         arrs.append(pice)
         arr   = arr[size:]
     arrs.append(arr)
     return arrs

print("==================split=====================")
jx = split(jrk_f1, 3)
print(jx)

print("++++++++++++++++opo iki++++++++++++++++++++++++++")
indx=[]
gf = []

for g in range(len(jx)):
    coba1 = np.min(jx[g])
    gf.append(coba1)
    for sd in range(len(jx)):
        for sf in range(3):
          
            if(coba1 == jx[sd][sf]):
                indx.append(sf)
            else:
                continue

print(gf)     
print(indx)


hg =[]        
print("==============================================------")
for gh in range(len(indx)):
    if(indx[gh] == 0):
        a="Iris-Setosa"
    elif(indx[gh] ==1):
        a="Iris-Versicolor"
    else:
        a="Iris-Virginica"
    hg.append(a)

print(hg)


print("================ITERASI 1======================")
pmbagi1=hg.count('Iris-Setosa')
pmbagi2=hg.count('Iris-Versicolor')
pmbagi3=hg.count('Iris-Virginica')
cb1 = []
cb2 = []
cb3 = []

for jk in range(len(f1)):
    if (indx[jk] == 0 ):
        cb1.append(f1[jk])
    else:
        continue
    

for jk in range(len(f1)):
    if (indx[jk] == 1 ):
        cb2.append(f1[jk])
    else:
        continue


for jk in range(len(f1)):
    if (indx[jk] == 2 ):
        cb3.append(f1[jk])
    else:
        continue

          
print(cb1)
print("======================================")
print(cb2)
print("======================================")
print(cb3)
centroid1=(sum(cb1)/pmbagi1)
centroid2=(sum(cb2)/pmbagi2)
centroid3=(sum(cb3)/pmbagi3)
print("================Centroid Baru======================")
print("             Fitur x")
print("Centroid 1 ",centroid1)
print("Centroid 2 ",centroid2)
print("Centroid 3 ",centroid3)

ca1 =[]
ca2 =[]
ca3 =[]


for jk in range(len(f2)):
    if (indx[jk] == 0 ):
        ca1.append(f2[jk])
    else:
        continue
    

for jk in range(len(f2)):
    if (indx[jk] == 1 ):
        ca2.append(f2[jk])
    else:
        continue


for jk in range(len(f2)):
    if (indx[jk] == 2 ):
        ca3.append(f2[jk])
    else:
        continue


centroid1a=(sum(ca1)/pmbagi1)
centroid2a=(sum(ca2)/pmbagi2)
centroid3a=(sum(ca3)/pmbagi3)
print("================Centroid Baru======================")
print("             Fitur y")
print("Centroid 1 ",centroid1a)
print("Centroid 2 ",centroid2a)
print("Centroid 3 ",centroid3a)

cx =[centroid1 ,centroid2, centroid3]
cy =[centroid1a , centroid2a,centroid3a]

jrk_f2 =[]
for i in range(150):
    for j in range(3):
        c1 = np.sqrt(((f1[i]-cx[j])**2)+((f2[i]-cx[j])**2))
        jrk_f2.append(c1)
        
print("================")
print(jrk_f2)
jjs = split(jrk_f2, 3)
print("================+++++++++++++++++++++++++++++++=================")
print(jjs)

indx1=[]
gf1 = []

for g in range(len(jx)):
    coba1 = np.min(jx[g])
    gf1.append(coba1)
    for sd in range(len(jx)):
        for sf in range(3):
          
            if(coba1 == jx[sd][sf]):
                indx1.append(sf)
            else:
                continue

print(gf1)     
print(indx1)


hg1 =[]        
print("==============================================------")
for gh in range(len(indx)):
    if(indx[gh] == 0):
        a="Iris-Setosa"
    elif(indx[gh] ==1):
        a="Iris-Versicolor"
    else:
        a="Iris-Virginica"
    hg1.append(a)

print(hg1)






print("================ITERASI 2======================")
cb1a = []
cb2a = []
cb3a = []

for jk in range(len(f1)):
    if (indx[jk] == 0 ):
        cb1a.append(f1[jk])
    else:
        continue
    

for jk in range(len(f1)):
    if (indx[jk] == 1 ):
        cb2a.append(f1[jk])
    else:
        continue


for jk in range(len(f1)):
    if (indx[jk] == 2 ):
        cb3a.append(f1[jk])
    else:
        continue

          
print(cb1a)
print("======================================")
print(cb2a)
print("======================================")
print(cb3a)
centroid1b=(sum(cb1a)/pmbagi1)
centroid2b=(sum(cb2a)/pmbagi2)
centroid3b=(sum(cb3a)/pmbagi3)
print("================Centroid Baru======================")
print("             Fitur x")
print("Centroid 1 ",centroid1b)
print("Centroid 2 ",centroid2b)
print("Centroid 3 ",centroid3b)

ca1b =[]
ca2b =[]
ca3b =[]


for jk in range(len(f2)):
    if (indx[jk] == 0 ):
        ca1b.append(f2[jk])
    else:
        continue
    

for jk in range(len(f2)):
    if (indx[jk] == 1 ):
        ca2b.append(f2[jk])
    else:
        continue


for jk in range(len(f2)):
    if (indx[jk] == 2 ):
        ca3b.append(f2[jk])
    else:
        continue


centroid1c=(sum(ca1b)/pmbagi1)
centroid2c=(sum(ca2b)/pmbagi2)
centroid3c=(sum(ca3b)/pmbagi3)
print("================Centroid Baru======================")
print("             Fitur y")
print("Centroid 1 ",centroid1c)
print("Centroid 2 ",centroid2c)
print("Centroid 3 ",centroid3c)

cx =[centroid1b ,centroid2b, centroid3b]
cy =[centroid1c , centroid2c,centroid3c]

jrk_f3 =[]
for i in range(150):
    for j in range(3):
        c1 = np.sqrt(((f1[i]-cx[j])**2)+((f2[i]-cx[j])**2))
        jrk_f3.append(c1)
        
print("================")
print(jrk_f3)
jjs1 = split(jrk_f3, 3)
print("================+++++++++++++++++++++++++++++++=================")
print(jjs1)

indx2=[]
gf2 = []

for g in range(len(jx)):
    coba1 = np.min(jx[g])
    gf2.append(coba1)
    for sd in range(len(jx)):
        for sf in range(3):
          
            if(coba1 == jx[sd][sf]):
                indx2.append(sf)
            else:
                continue

print(gf2)     
print(indx2)


hg2 =[]        
print("==============================================------")
for gh in range(len(indx)):
    if(indx[gh] == 0):
        a="Iris-Setosa"
    elif(indx[gh] ==1):
        a="Iris-Versicolor"
    else:
        a="Iris-Virginica"
    hg2.append(a)

print(hg2)

plt.subplot(221)
plt.scatter(C_x, C_y, marker='*',s=200, c='g')
plt.scatter(f1,f2  , color='black')

plt.subplot(222)
plt.scatter(centroid1, centroid1a, marker='*',s=200, c='red')
plt.scatter(centroid2, centroid2a, marker='*',s=200, c='red')
plt.scatter(centroid3, centroid3a, marker='*',s=200, c='red')
plt.scatter(f1,f2  , color='black')

plt.subplot(223)
plt.scatter(centroid1b, centroid1c, marker='*',s=200, c='red')
plt.scatter(centroid2b, centroid2c, marker='*',s=200, c='red')
plt.scatter(centroid3b, centroid3c, marker='*',s=200, c='red')
plt.scatter(f1,f2  , color='black')

plt.show()
print("==============================================------")

if(hg1 == hg2):
        print("masok")
else:
    print("ndak")



#cetroid2=

#centroid3=

        
#fig = plt.figure(figsize=(5, 5))
#data.plot.scatter(x='avail_seat_km_per_week' , y='fatalities_00_14', marker='o', color='black')

##plt.xlim(0, 80)
#plt.ylim(0, 80)
#plt.show()

 