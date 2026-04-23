import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
from scipy.signal import lfilter
import Guia2.funcConvolucion as fc

def main():
    
    _ , x = f1.generar_senoidal(fs = 5,fm = 30 ,phi = 0,t_inicio = 0, t_fin = 2)
    h = np.array([0.0, 0.0, 0.0, 0.0, 1.0])
    
    y_manual = fc.convolucion(x=x, h=h)
    y_conv = np.convolve(x, h, mode='full')
    y_filter = lfilter(b=h, a=[1.0], x=x) # Corrección: a=[1.0]

    # N muestras de entrada, M de respuesta al impulso
    N, M = len(x), len(h)
    L = N + M - 1 # Longitud de la convolución lineal completa
    
    n_x = np.arange(N)
    n_h = np.arange(M)
    n_y = np.arange(L)

    # 4. Configuración de la visualización (5 gráficos separados)
    plt.figure(figsize=(12, 20)) # Ajustamos el alto para que no se pisen los títulos

    # --- Gráfico 1: Entrada ---
    plt.subplot(5, 1, 1)
    plt.stem(n_x, x, basefmt="black", linefmt="C0", markerfmt="C0o")
    plt.title('Señal de Entrada x[n]', fontweight='bold')
    plt.grid(True)
    plt.xlim(-1, L+1) # Mismo eje X para comparar alineación

    # --- Gráfico 2: Respuesta al Impulso ---
    plt.subplot(5, 1, 2)
    plt.stem(n_h, h, basefmt="black", linefmt="C1", markerfmt="C1o")
    plt.title('Respuesta al Impulso h[n] (Filtro)', fontweight='bold')
    plt.grid(True)
    plt.xlim(-1, L+1)

    # --- Gráfico 3: np.convolve (Referencia) ---
    plt.subplot(5, 1, 3)
    plt.stem(n_y, y_conv, basefmt="black", linefmt="C2", markerfmt="C2o")
    plt.title('Convolución de NumPy', fontweight='bold')
    plt.grid(True)
    plt.xlim(-1, L+1)

    # --- Gráfico 4: Tu Convolución Manual ---
    plt.subplot(5, 1, 4)
    plt.stem(n_y, y_manual, basefmt="black", linefmt="C3", markerfmt="C3o")
    plt.title('Convolución Propia', fontweight='bold')
    plt.grid(True)
    plt.xlim(-1, L+1)

    # lfilter
    plt.subplot(5, 1, 5)
    plt.stem(n_x, y_filter, basefmt="black", linefmt="C4", markerfmt="C4o")
    plt.title('Salida de lfilter', fontweight='bold')
    plt.xlabel('Número de muestras (n)')
    plt.grid(True)
    plt.xlim(-1, L+1)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()