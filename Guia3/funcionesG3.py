import numpy as np
import matplotlib as plot
from scipy.special import legendre

def Norma(x,p=2):
    if(p == "inf"):
        return max(np.abs(x))
    x_elevado = np.abs(x) ** p
    x_sum = np.sum(x_elevado)
    y = x_sum ** (1/p)
    return y

def calcular_termino_legendre(n, t, y):
    """
    Calcula el coeficiente alfa_n y la base phi_n(t) de Legendre 
    para una señal discreta y(t).
    """
    dt = t[1] - t[0] # Ancho de paso para la integral
    
    # Generamos la base normalizada phi_n(t)
    phi_n = np.sqrt((2*n + 1) / 2) * legendre(n)(t)
    
    # Calculamos el coeficiente alfa_n (aproximación de la integral)
    alfa_n = np.sum(phi_n * y) * dt
    
    return alfa_n, phi_n