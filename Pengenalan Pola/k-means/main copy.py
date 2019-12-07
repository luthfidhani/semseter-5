"""
Code by Luthfi A. A.
"""
import pandas as pd
import numpy as np
import random
import time
import matplotlib.pyplot as plt

#=========== Membaca Excel ==========#
data = pd.read_excel (r'Iris.xls')
#=========== Membaca Setiap Kolom ==========#
f1 = pd.DataFrame(data, columns = ['SepalLengthCm'])
f2 = pd.DataFrame(data, columns = ['SepalWidthCm'])
f3 = pd.DataFrame(data, columns = ['PetalLengthCm'])
f4 = pd.DataFrame(data, columns = ['PetalWidthCm'])

#=========== Digabung Jadi 1 Array ==========#
data = np.hstack((f1, f2, f3, f4))
# print (data[2,1]) #data[baris,kolom]

#=========== random centroid ==========#
# c1 = np.hstack((random.choice(data[:,0]), random.choice(data[:,1]), random.choice(data[:,2]), random.choice(data[:,3])))
# c2 = np.hstack((random.choice(data[:,0]), random.choice(data[:,1]), random.choice(data[:,2]), random.choice(data[:,3])))
# c3 = np.hstack((random.choice(data[:,0]), random.choice(data[:,1]), random.choice(data[:,2]), random.choice(data[:,3])))
c1 = [6.3, 3.8, 3.7, 0.2]
c2 = [6.4, 3. , 6.1, 1.4]
c3 = [6.7, 3.4, 1.4, 1.9]


#centroid = [setosia, versicolor, virginica]
centroid = [c1, c2, c3]

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
hasil_angka = []
hasil_huruf = []
for i in range (len(jarak)):
    a = np.min(jarak[i])
    #=========== menentukan kelas ==========#
    if(a==jarak[i][0]):
        b = 1
        c = "setosia"
    elif(a == jarak[i][1]):
        b = 2
        c = "versicolor"
    else :
        b = 3
        c = "virginica"
    angka = [a, b]
    huruf = [a, c]
    hasil_angka.append(angka)
    hasil_huruf.append(huruf)
min_class = hasil_angka
min_class_huruf = hasil_huruf
print("#================== Iterasi 0 ==================#")
print("    f1   f2    f3    f4     c1     c2     c3     min      kelas")
# print("  f1   f2   f3   f4   c1    c2  c3   min kelas")   
gabung_huruf = np.hstack((f1, f2, f3, f4, jarak, min_class_huruf))
print(gabung_huruf)

gabung = np.hstack((f1, f2, f3, f4, jarak, min_class))

a = gabung
# print(a)
#=========================================================#
centro = True
#=========== next iterasi ==========#

#=========== menentukan centroid ==========#
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
        c2_f1 = c2_f1+ a[i,0]  
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

c1 = np.round([c1_f1, c1_f2, c1_f3, c1_f4],2)
c2 = np.round([c2_f1, c2_f2, c2_f3, c2_f4],2)
c3 = np.round([c3_f1, c3_f2, c3_f3, c3_f4],2)

cent1 = np.true_divide(c1, count_c1)
cent2 = np.true_divide(c2, count_c2)
cent3 = np.true_divide(c3, count_c3)

centroid =[cent1, cent2, cent3]
print("#=========== centroid selanjutnya ==========#")
print(centroid)
