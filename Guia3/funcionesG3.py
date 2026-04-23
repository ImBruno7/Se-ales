import numpy as np
import matplotlib as plot

def Norma(x,p=2):
    if(p == "inf"):
        return max(np.abs(x))
    x_elevado = np.abs(x) ** p
    x_sum = np.sum(x_elevado)
    y = x_sum ** (1/p)
    return y