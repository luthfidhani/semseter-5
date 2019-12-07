import pandas as pd
import numpy as np
import random
import time
import matplotlib.pyplot as plt

a = [1.222249, 2.65689595, 3.6519849489]
b = [7, 8, 9]

c = np.hstack((a,b))

print(c)



# h = np.true_divide(a, 4)
# print(h)
# a = 5
# if (a==5):
#     g = "sdsdsdsd"
# print(g)

i = 1

while True:
    print("Iterasi ke = ",i)
    i = i + 1
    if(i > 3):
        break