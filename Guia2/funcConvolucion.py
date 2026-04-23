import numpy as np
import matplotlib.pyplot as plt

def convolucion(x,h):
    N = len(x)
    M = len(h)
    L = N + M - 1
    y = np.zeros(L)
    
    for n in range(L):
        for k in range (N):
            if (n - k) >= 0 and (n - k) < M :
                y[n] += x[k] * h[n - k]

    return y


def convCircular(x,h):
    N = len(x)
    y = np.zeros(N)

    for k in range(N):
        for l in range(N):
            y[k] += h[l]*x[np.mod(k-l,N)] 

    return y