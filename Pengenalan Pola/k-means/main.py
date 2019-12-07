"""
Code by Luthfi A. A.
"""
import pandas as pd
import numpy as np
import random
import time
import matplotlib.pyplot as plt

#=========== Membaca Excel ==========#
data = pd.read_excel (r'Iris copy.xls')
#=========== Membaca Setiap Kolom ==========#
f1 = pd.DataFrame(data, columns = ['SepalLengthCm'])
f2 = pd.DataFrame(data, columns = ['SepalWidthCm'])
f3 = pd.DataFrame(data, columns = ['PetalLengthCm'])
f4 = pd.DataFrame(data, columns = ['PetalWidthCm'])

#=========== Digabung Jadi 1 Array ==========#
data = np.hstack((f1, f2, f3, f4))
# print (data[2,1]) #data[baris,kolom]

#=========== random centroid ==========#
c1 = np.hstack((random.choice(data[:,0]), random.choice(data[:,1]), random.choice(data[:,2]), random.choice(data[:,3])))
c2 = np.hstack((random.choice(data[:,0]), random.choice(data[:,1]), random.choice(data[:,2]), random.choice(data[:,3])))
c3 = np.hstack((random.choice(data[:,0]), random.choice(data[:,1]), random.choice(data[:,2]), random.choice(data[:,3])))
# c1 = [4.9, 2.8, 5.2, 1.4]
# c2 = [5.4, 3.2, 6.4, 0.2]
# c3 = [7.7, 3. , 3.3, 2.5]

centro = False

balik=1
while True:
    #=========== menentukan centroid ==========#
    print(centro)
    if (centro == True):
        count_c1 = 0
        c1_f1 = 0 
        c1_f2 = 0
        c1_f3 = 0 
        c1_f4 = 0
        count_c2 = 0
        c2_f1 = 0 
        c2_f2 = 0
        c2_f3 = 0 
        c2_f4 = 0
        count_c3 = 0
        c3_f1 = 0 
        c3_f2 = 0
        c3_f3 = 0 
        c3_f4 = 0

        for i in range(len(a)):
            if(a[i,8] == 1):
                c1_f1 = c1_f1 + a[i,0]  
                c1_f2 = c1_f2 + a[i,1]  
                c1_f3 = c1_f3 + a[i,2]  
                c1_f4 = c1_f4 + a[i,3]  
                count_c1 = count_c1 + 1
                
            elif(a[i,8] == 2):
                c2_f1 = c2_f1 + a[i,0]  
                c2_f2 = c2_f2 + a[i,1]  
                c2_f3 = c2_f3 + a[i,2]  
                c2_f4 = c2_f4 + a[i,3]
                count_c2 = count_c2 + 1

            else:
                c3_f1 = c3_f1 + a[i,0]  
                c3_f2 = c3_f2 + a[i,1]  
                c3_f3 = c3_f3 + a[i,2]  
                c3_f4 = c3_f4 + a[i,3]
                count_c3 = count_c3 + 1

        cent1 = [c1_f1, c1_f2, c1_f3, c1_f4]
        cent2 = [c2_f1, c2_f2, c2_f3, c2_f4]
        cent3 = [c3_f1, c3_f2, c3_f3, c3_f4]

        c1 = np.round(np.true_divide(cent1, count_c1),2)
        c2 = np.round(np.true_divide(cent2, count_c2),2)
        c3 = np.round(np.true_divide(cent3, count_c3),2)
    #=========== end of menentukan centroid ==========#

    #centroid = [setosia, versicolor, virginica]
    centroid = [c1, c2, c3]
    print("#=========== centroid ==========#")
    print(centroid)
    print("#===============================#")

    # print(len(centroid))
    #=========== perhitungan jarak eukledian ==========#
    euclidean=[]
    for i in range(len(data)): #looping data
        for j in range(len(centroid)): #looping centroid
            a = np.sqrt(sum(np.power(np.subtract(data[i,j],centroid[j]),2)))
            euclidean.append(a)
    

    def split(arr, size):
        arrs = []
        while len(arr) > size:
            pice = arr[:size]
            arrs.append(pice)
            arr   = arr[size:]
        arrs.append(arr)
        return arrs

    jarak = np.round(split(euclidean, len(centroid)),2)

    #=========== menentukan jarak minimum dan kelas ==========#
    hasil = []
    for i in range (len(jarak)):
        a = np.min(jarak[i])
        #=========== menentukan kelas ==========#
        if(a==jarak[i][0]):
            b = 1
        elif(a == jarak[i][1]):
            b = 2
        else :
            b = 3
        c = [a, b]
        hasil.append(c)
    min_class = hasil
    # print("    f1   f2    f3    f4     c1     c2     c3     min      kelas")
    print("  f1   f2   f3   f4   c1    c2  c3   min kelas")   
    gabung = np.hstack((f1, f2, f3, f4, jarak, min_class))
    a = gabung
    for i in range(len(a)):
        print(a[i])
    #=========================================================#
    centro = True
    print("#=========== next iterasi ==========#")

    balik = balik+1
    if(balik>5):
        break
