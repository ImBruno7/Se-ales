import numpy as np
import matplotlib as plot

def generar_senoidal(fs, fm, phi, t_inicio, t_fin):
    """
    fs: Frecuencia de la senoidal (Hz)
    fm: Frecuencia de muestreo (Hz)
    phi: Fase inicial (radianes)
    t_inicio: Tiempo inicial (s)
    t_fin: Tiempo final (s)
    """
    #paso = 1 / fm # Definimos el paso de tiempo (1/fm)
    
    # Creamos el vector de tiempo t desde t_inicio hasta t_fin inclusive (np.arange para mantener el paso constante)
    num_muestras = int((t_fin - t_inicio) * fm) + 1
    t = np.linspace(t_inicio, t_fin, num_muestras)
    
    # Ecuación: y(t) = sen(2π * fs * t + phi)
    y = np.sin(2 * np.pi * fs * t + phi)
    
    return t, y

def generar_sync(fs, fm, t_inicio, t_fin):
    paso = 1 / fm
    t = np.arange(t_inicio, t_fin+paso, paso)
    x = 2 * np.pi * fs * t
    y = np.where(x!=0,np.sin(x)/x,1.0)

    return t,y

def generar_onda_cuadrada(fs, fm, phi, t_inicio, t_fin):
    paso = 1 / fm
    t = np.arange(t_inicio, t_fin+paso, paso)
    x = np.mod(2 * np.pi * fs * t + phi,2 * np.pi)
    y = np.where(x<np.pi,1.0,-1.0)

    return t,y


def sinc_interpoladora(x):
    pi_x = np.pi * x
    return np.where(pi_x != 0, np.sin(pi_x) / pi_x, 1.0)

def interpolar(x,y,fm0,fm1,func):
    T = 1/fm0
    
    #generamos el nuevo x
    duracion = x[-1] - x[0] # Esto da 2 si vas de 0 a 2
    n_puntos = int(duracion * fm1) + 1
    x_nuevo = np.linspace(x[0], x[-1], n_puntos)

    
    y_nuevo = []

    # Para cada tiempo nuevo, calculamos la sumatoria
    for ti in x_nuevo:
        # (ti - nT) / T  <-- Esto es un vector de distancias
        argumento = (ti - x) / T
        
        # Aplicamos la función sinc nuestra
        pesos = func(argumento)
        
        # Sumatoria: y_orig[n] * sinc(...)
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