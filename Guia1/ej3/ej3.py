import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1

def main():
    fm = 900      # Frecuencia de muestreo (Hz)
    fs=20
    phi = -(2/9) * np.pi
    A=3

    t_i, t_f = 0, 0.1 # Intervalo [0, 1] segundos

    t1, y1 = f1.generar_senoidal(fs, fm, phi, t_i, t_f)
    y1 = np.multiply(y1,A)

    plt.figure(figsize=(12, 10))

    plt.stem(t1, y1)
    plt.title("1. Señal Original ($f_s=5Hz$)")
    plt.grid(True)
    plt.ylabel("Amplitud")
    plt.tight_layout()
    plt.show()


main()