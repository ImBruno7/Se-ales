import numpy as np
import matplotlib as plot
from scipy.special import legendre
import Guia1.ej1.funciones as f1

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

def generar_base(frecuencias,phi,fm,t_fin):
    base = [] 
    for i in range(len(frecuencias)):
        _, s_aux = f1.generar_senoidal(fs = frecuencias[i], fm = fm, phi = phi[i], t_inicio = 0, t_fin = t_fin)
        base.append(s_aux)
    
    return base

def obtener_mejor_frecuencia(signal, frecuencias):
    """
    Barre una lista de frecuencias y fases para encontrar la que tiene
    el mayor producto interno con la senial.
    """
    fm = 11025
    duracion_signal = (len(signal)-1) / fm 
    angulos_fase = np.linspace(0, 2*np.pi, 20, endpoint=False)
    
    max_similitud_global = 0
    freq_ganadora = 0
    
    for freq in frecuencias:
        max_similitud_freq = 0
        
        # Buscamos la mejor fase para ESTA frecuencia
        for angulo in angulos_fase:
            t, base = f1.generar_senoidal(fs=freq, fm=fm, phi=angulo, t_inicio=0, t_fin=duracion_signal)
            similitud = abs(np.sum(signal * base))
            
            # Nos quedamos con el mejor puntaje de esta frecuencia en particular
            if similitud > max_similitud_freq:
                max_similitud_freq = similitud
                
        # Comparamos si el mejor puntaje de esta frecuencia le gana al récord global
        if max_similitud_freq > max_similitud_global:
            max_similitud_global = max_similitud_freq
            freq_ganadora = freq
            
    return freq_ganadora