import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1

def H(z,n):
    if(n==1):
        h = 1 / (1- (1/2)* (z**-1) + (1/4)*(z**-2) )
        return h
    if(n==2):
        h = (z**-1) / (1 - (z**-1) - (z**-2) )
        return h
    if(n==3):
        h = 7 / (1- 2* (z**-1) + 6*(z**-2) )
        return h
    else:
       # Armamos la sumatoria del filtro FIR
        h = np.zeros_like(z, dtype=complex) #copia len y estructura
        for k in range(8):
            h += (2**-k) * (z**-k)
        return h
    


def main():
    fm = 10000                                    
    f = np.linspace(-fm/2, fm/2, 1000)                  # Vector de frecuencias (0 a Nyquist)

    z = np.exp(1j * 2 * np.pi * f / fm)

    fig, axs = plt.subplots(2, 2, figsize=(14, 9))
    fig.suptitle('Respuesta en Frecuencia de los Sistemas LTI', fontsize=16, fontweight='bold')
    
    colores = ['blue', 'green', 'red', 'purple']

    for i in range(4):
        n = i + 1                                   # Sistema 1, 2, 3 o 4
        h_n = H(z, n)                               # Llamamos a tu función
        magnitud = np.abs(h_n)                      # Módulo de la función de transferencia
        

        fila = i // 2 #esto es para el grafico nomas
        columna = i % 2 #esto es para el grafico nomas
        
        axs[fila, columna].plot(f, magnitud, color=colores[i], linewidth=2)
        axs[fila, columna].set_title(f'Sistema {n}')
        axs[fila, columna].set_xlabel('Frecuencia [Hz]')
        axs[fila, columna].set_ylabel('Magnitud |H(f)|')
        axs[fila, columna].grid(True, linestyle=':')
        
        axs[fila, columna].set_xlim(-fm/2, fm/2)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()