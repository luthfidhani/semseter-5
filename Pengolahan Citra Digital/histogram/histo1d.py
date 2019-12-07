import numpy as np
import matplotlib.pyplot as plt
def histgram(f):
    n = f.shape[0]
    #misal ukuran histogram L = 4
    h = np.zeros(8)
    for i in range(n):
        h[f[i]] += 1
    return(h)

def RUN():
    f = np.array([0,0,1,1,1,1,1,1,0,0,2,2,2,2,2,1,1,1,2,2,2,2,2,2,4,3,2,5,4,4,5,5,3,3,2,5,4,4,5,5,2,2,1,1,0,0,0,0,1,1,4,4,5,5,2,3,2,3,2,4,4])
    histo = histgram(f)
    print('f : ', f)
    print('histogram : ', histo)

    plt.style.use('ggplot')
    plt.hist(f, bins=4)
    plt.show()

if __name__ == "__main__":
    RUN()