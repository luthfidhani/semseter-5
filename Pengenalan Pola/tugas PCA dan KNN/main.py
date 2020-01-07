"""
Code by Luthfi A. A.
"""
import pandas as pd
from scipy import stats 
import numpy as np

data = pd.read_excel (r'forecast.xlsx')

SuhuMax = pd.DataFrame(data, columns= ['suhu max'])
meanSuhuMax = float(SuhuMax.mean())
matrixSuhuMax = SuhuMax.as_matrix()

SuhuMin = pd.DataFrame(data, columns= ['suhu min'])
meanSuhuMin = float(SuhuMin.mean())
matrixSuhuMin = SuhuMin.as_matrix()

Kelembapan = pd.DataFrame(data, columns= ['kelembapan'])
meanKelembapan = float(Kelembapan.mean())
matrixKelembapan = Kelembapan.as_matrix()

Presipitasi = pd.DataFrame(data, columns= ['presipitasi'])
meanPresipitasi = float(Presipitasi.mean())
matrixPresipitasi = Presipitasi.as_matrix()

Angin = pd.DataFrame(data, columns= ['angin'])
meanAngin = float(Angin.mean())
matrixAngin = Angin.as_matrix()

Uv = pd.DataFrame(data, columns= ['uv'])
meanUv = float(Uv.mean())
matrixUv = Uv.as_matrix()

Prediksi = pd.DataFrame(data, columns= ['prediksi'])
matrixPrediksia = Prediksi.as_matrix()
matrixPrediksi = matrixPrediksia[0:10]

#=========== Mendapatkan D ==========#
matrixD = np.hstack((matrixSuhuMax, matrixSuhuMin, matrixKelembapan, matrixPresipitasi, matrixAngin, matrixUv))
#print ("\nMatrix D \n", matrixD)

#=========== Mencari Mean Setiap Fitur ==========#
average = np.hstack((meanSuhuMax, meanSuhuMin, meanKelembapan, meanPresipitasi, meanAngin, meanUv))
#print ("\nRata-Rata setiap fitur\n", average)

#=========== Mencari ZeroMean ==========#
zeroMean = np.subtract(matrixD, average)
#print("\nZeroMean\n",zeroMean)

#=========== Menghitung Coev ==========#
n = len(zeroMean[0])
coev = 1/(n-1)*(np.transpose(zeroMean).dot(zeroMean))
#print("\nCoev\n",coev)

#=========== Menghitung Nilai Eigen dan Eigen Vector ==========#
w, v = np.linalg.eig(coev)
#print("\nEigen Value\n",w) #value
#print("\nEigen Vector\n",v) #vector

wSort = sorted(w, reverse = True)
#print("\nEigen Value Sorted\n",wSort)

#=========== Mempertahankan 75% data ==========#
i=0
lamb=0
for i in range(len(w)):
    lamb += wSort[i]
    i += 1

keep = (75/100) * lamb


i2 = 0
j2 = 0
for i2 in range(len(w)):
    j2 += wSort[i2]
    i2 += 1
    if j2 > keep:
        break

newEgVec = v[0:len(v),0:i2]

fiturBaru = np.transpose(np.transpose(newEgVec).dot(np.transpose(zeroMean)))
#print("\nFitur Baru 75%\n",fiturBaru)
#print("\n================== END OF PCA ==================\n")

print("\n================== WEIGHTED-KNN ==================\n")

dataSet = fiturBaru[0:10,:]
dataTesting = fiturBaru[10:11,:]

print("\nData Set\n",dataSet)
print("\nData Testing\n",dataTesting)

hitungSetTes  = np.subtract(dataTesting, dataSet)
powerSetTes = np.power(hitungSetTes, 2)


l1 = powerSetTes[:,0:1]
l2 = powerSetTes[:,1:2]
print("\nl1\n", l1)
print("\nl2\n", l2)

addSetTes = np.add(l1,l2)
print("\nDitambahkan\n", addSetTes)

sqrtSetTes = np.sqrt(addSetTes)
print("\nJarak\n", sqrtSetTes)

balikan = np.hstack((sqrtSetTes, matrixPrediksi))
print(balikan)

h1 = 0
h2 = 0
for i in range(len(balikan)):
    if balikan[i,1] == 0:
        h1 = h1 + (1/np.power(balikan[i,0],2))
    else:
        h2 = h2 + (1/np.power(balikan[i,0],2))


print("\nVote Sunny = ", h1)
print("\nVote Cloudy = ", h2)
print("\nThe Answer is")

if h1 > h2 :
    print("Sunny")
else:
    print("Cloudy")

