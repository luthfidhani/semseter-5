import pandas as pd
from scipy import stats 
import numpy as np

data = pd.read_excel (r'pawang_hujan.xlsx')

suhu = pd.DataFrame(data, columns= ['suhu'])
#meansuhu = suhu.mean()
matrixsuhu = suhu.as_matrix()

a = 0
n = 0
for t in range(len(suhu)):
    a = a + matrixsuhu[t]
    n = n + 1
meansuhu = a/n
#print(meansuhu)

kelembapan = pd.DataFrame(data, columns= ['kelembapan'])
#meankelembapan = kelembapan.mean()
matrixkelembapan = kelembapan.as_matrix()
a = 0
n = 0
for b in range(len(kelembapan)):
    a = a + matrixkelembapan[b]
    n = n + 1
meankelembapan = a/n
#print(meankelembapan)

angin = pd.DataFrame(data, columns= ['angin'])
#eanangin = angin.mean()
matrixangin = angin.as_matrix()
a = 0
n = 0
for u in range(len(angin)):
    a = a + matrixangin[u]
    n = n + 1
meanangin = a/n
#print(meanangin)

polusi = pd.DataFrame(data, columns= ['polusi'])
#eanpolusi = polusi.mean()
matrixpolusi = polusi.as_matrix()
a = 0
n = 0
for u in range(len(polusi)):
    a = a + matrixpolusi[u]
    n = n + 1
meanpolusi = a/n
#print(meanpolusi)

pawang = pd.DataFrame(data, columns= ['pawang'])
#eanangin = pawang.mean()
matrixpawang = pawang.as_matrix()
a = 0
n = 0
for u in range(len(pawang)):
    a = a + matrixpawang[u]
    n = n + 1
meanpawang = a/n
#print(meanpawang)



#=========== Mendapatkan D ==========#
matrixD = np.hstack((matrixsuhu, matrixkelembapan, matrixangin, matrixpolusi, matrixpawang))
Average = [[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang],
[meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang]]
print ("\nMatrix D \n", matrixD)

#=========== Mencari Mean Setiap Fitur ==========#
average = np.hstack((meansuhu, meankelembapan, meanangin, meanpolusi, meanpawang))
print ("\nRata-Rata setiap fitur\n", average)

#=========== Mencari ZeroMean ==========#
zeroMean = np.subtract(matrixD, average)
print("\nZeroMean\n",zeroMean)

#for d in range(len(matrixD)):
#    for v in range(len(average)):
#        hasil = matrixD[d][v] - average [v]
#        print (hasil, end =' ')
#    print('\n')

#=========== Menghitung Coev ==========#
n = len(zeroMean[0])
coev = 1/(n-1)*(np.transpose(zeroMean).dot(zeroMean))
print("\nCoev\n",coev)

#=========== Menghitung Nilai Eigen dan Eigen Vector ==========#
w, v = np.linalg.eig(coev)
print("\nEigen Value\n",w) #value
print("\nEigen Vector\n",v) #vector

wSort = sorted(w, reverse = True)
print(wSort)

#=========== Mempertahankan 88% data ==========#
i=0
lamb=0
for i in range(len(w)):
    lamb += wSort[i]
    i += 1
#print(lamb)

#print(w[0] + w[1] + w[2])
hold = (88/100) * lamb
#print(hold)

i2 = 0
j2 = 0
for i2 in range(len(w)):
    j2 += wSort[i2]
    i2 += 1
    if j2 > hold:
        break

newEgVec = v[0:len(v),0:i2]
print(newEgVec)

#print(np.transpose(newEgVec))
fiturBaru = np.transpose(np.transpose(newEgVec).dot(np.transpose(zeroMean)))
print("\nFitur Baru\n",fiturBaru)