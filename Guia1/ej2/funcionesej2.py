import numpy as np
import matplotlib.pyplot as plt

def inversion(xn,yn):
    return np.negative(xn),yn   

def rectificacion(yn,type="onda_completa"):
    if(type=="onda_completa"):
        return np.absolute(yn)
    if(type=="onda_media"):
        return np.where(yn<0,0,yn)


def cuantizacion(yn,N=8):
    aux = np.min(yn)
    rango = np.max(yn)-aux
    H = rango / (N-1)

    yn = np.add(yn,-aux) #movemos el nivel mas bajo a 0
    
    yn = np.where(yn<0,0,np.where(yn<(N-1)*H,H*(np.floor(yn/H)),(N-1)*H))

    yn = np.add(yn,aux) #volvemos a la amplitud o nivel real

    return yn


