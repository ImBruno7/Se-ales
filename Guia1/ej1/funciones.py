import numpy as np
import matplotlib as plot

def generar_senoidal(A, fs, fm, phi, t_inicio, t_fin):
    """
    fs: Frecuencia de la senoidal (Hz)
    fm: Frecuencia de muestreo (Hz)
    phi: Fase inicial (radianes)
    t_inicio: Tiempo inicial (s)
    t_fin: Tiempo final (s)
    """
    num_muestras = int((t_fin - t_inicio) * fm)
    
    t = np.arange(num_muestras) / fm + t_inicio
    
    # Ecuación: y(t) = sen(2π * fs * t + phi)
    y = np.sin(2 * np.pi * fs * t + phi)
    
    return t, A*y

def generar_sync(fs, fm, t_inicio, t_fin):
    num_muestras = int((t_fin - t_inicio) * fm)
    
    t = np.arange(num_muestras) / fm + t_inicio
    x = 2 * np.pi * fs * t
    y = np.where(x!=0,np.sin(x)/x,1.0)

    return t,y

def generar_onda_cuadrada(fs, fm, phi, t_inicio, t_fin):
    num_muestras = int((t_fin - t_inicio) * fm)
    
    t = np.arange(num_muestras) / fm + t_inicio
    x = np.mod(2 * np.pi * fs * t + phi,2 * np.pi)
    y = np.where(x<np.pi,1.0,-1.0)

    return t,y


def sinc_interpoladora(x):
    pi_x = np.pi * x
    return np.where(pi_x != 0, np.sin(pi_x) / pi_x, 1.0)

def interpolar(x,y,fm0,fm1,func):
    """
    x: Vector de tiempo original (baja resolución)
    y: Valores de la señal original
    fm0: Frecuencia de muestreo original
    fm1: Frecuencia de muestreo nueva (alta resolución)
    func: Función kernel (usualmente sinc_interpoladora)
    """
    T = 1 / fm0
    duracion = len(x) / fm0
    
    # Generamos el nuevo eje x 
    n_puntos = int(duracion * fm1)
    x_nuevo = np.arange(n_puntos) / fm1 + x[0]
    
    y_nuevo = []

    for ti in x_nuevo:
        # Calculamos la distancia de cada punto nuevo a todos los puntos originales
        # (ti - nT) / T
        argumento = (ti - x) / T
        
        # Obtenemos los pesos usando el kernel (sinc)
        pesos = func(argumento)
        
        # La sumatoria: cada muestra original aporta un poquito a la nueva
        valor_interp = np.sum(y * pesos)
        y_nuevo.append(valor_interp)

    return x_nuevo, np.array(y_nuevo)


def generar_un_valor_gaussiano(media, varianza):
    
    # Generamos el valor "base" (media 0, varianza 1) sumando 12 uniformes
    suma = 0
    for _ in range(12):
        numero_al_azar = np.random.uniform(0, 1)
        suma += numero_al_azar
    
    valor_base = suma - 6
    
    # Calculamos el desvío estándar
    desvio = np.sqrt(varianza)
    
    # Transformamos el valor base segun los datos
    valor_final = media + (valor_base * desvio)
    
    return valor_final

def generar_ruido(n,media,varianza):
    return np.array([generar_un_valor_gaussiano(media, varianza) for _ in range(n)])