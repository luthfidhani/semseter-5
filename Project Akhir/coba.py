import pandas as pd
import numpy as np

data = pd.read_excel(r'data fixx.xlsx')


f1 = pd.DataFrame(data, columns = ['slg'])
f2 = pd.DataFrame(data, columns = ['goa_maria'])
f3 = pd.DataFrame(data, columns = ['kebun_matahari'])
f4 = pd.DataFrame(data, columns = ['goa_selomangleng'])
f5 = pd.DataFrame(data, columns = ['gunung_klotok'])
f6 = pd.DataFrame(data, columns = ['bdi'])
f7 = pd.DataFrame(data, columns = ['alun_kediri'])
f8 = pd.DataFrame(data, columns = ['taman_sekartaji'])
f9 = pd.DataFrame(data, columns = ['klenteng'])

data = np.hstack((f1,f2,f3,f4,f5,f6,f7,f8,f9))

tau = 0.021

#============== Nilai Visibilitas ==============#
visibilitas = np.round(np.divide(1,data, out = np.zeros_like(data), where=data!=0),4)


#============== Probabilitas ==============#

to_modify = [5,4,3,2,1,0]
indexes =   [0,1,3,5,5,7]

print(np.array(to_modify) + np.array(indexes))