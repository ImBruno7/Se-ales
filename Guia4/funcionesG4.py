import numpy as np

def procesar_y_centrar(señal, fm):
    """
    Calcula la TDF, centra el espectro manualmente y devuelve 
    ejes de frecuencia y magnitud normalizada.
    """
    n = len(señal)
    # 1. Calculamos la TDF
    S_k = np.fft.fft(señal)
    
    # 2. Centrado manual: la segunda mitad (frecuencias negativas) al principio
    S_centrado = np.concatenate((S_k[n//2:], S_k[:n//2]))
    
    # 3. Generamos eje de frecuencias centrado en 0
    f_centradas = np.linspace(-fm/2, fm/2, n, endpoint=False)
    
    # 4. Magnitud normalizada por N para ver amplitudes reales
    magnitud = np.abs(S_centrado) / n
    
    return f_centradas, magnitud, S_k