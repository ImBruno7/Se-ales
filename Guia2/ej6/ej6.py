import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia2.funcConvolucion as fc

    
def main():
    N = 30
    n_x = np.arange(N)

    # Campana de Gauss
    x = np.exp(-0.5 * ((n_x - 7) / 2.0)**2)

    # Señal h: Un retardo zarpado en n=22 que empuja la montañita 20 lugares hacia la derecha
    h = np.zeros(N)
    h[22] = 1.0
    h[10] = 1.0

    # Calculamos ambas convoluciones
    y_circular = fc.convCircular(x, h)
    
    y_lineal = fc.convolucion(x, h)
    n_lin = np.arange(len(y_lineal))

    # Gráficas Aesthetic
    plt.figure(figsize=(10, 8))

    # Señal Original
    plt.subplot(3, 1, 1)
    plt.fill_between(n_x, x, color="skyblue", alpha=0.4) # Sombreado lindo
    plt.stem(n_x, x, basefmt="black", linefmt="dodgerblue", markerfmt="bo")
    plt.title('Señal original x[n]', fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlim(-1, 50)
    plt.ylim(-0.1, 1.2)

    # Convolución Lineal
    plt.subplot(3, 1, 2)
    plt.fill_between(n_lin, y_lineal, color="lightgreen", alpha=0.4)
    plt.stem(n_lin, y_lineal, basefmt="black", linefmt="limegreen", markerfmt="go")
    plt.title('Convolución Lineal', fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlim(-1, 50)
    plt.ylim(-0.1, 1.2)

    # Convolución Circular
    plt.subplot(3, 1, 3)
    plt.fill_between(n_x, y_circular, color="salmon", alpha=0.4)
    plt.stem(n_x, y_circular, basefmt="black", linefmt="crimson", markerfmt="ro")
    plt.title('Convolución Circular', fontweight='bold')
    plt.xlabel('Muestras (n)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xlim(-1, 50)
    plt.ylim(-0.1, 1.2)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()