import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f

def main1():
    fm = 100       # Frecuencia de muestreo (Hz)
    t_i, t_f = 0, 1 # Intervalo [0, 1] segundos

    # Caso A: fs = 5 Hz (Cumple 2*fs <= fm), Fase = 0
    t1, y1 = f.generar_senoidal(5, fm, 0, t_i, t_f)

    # Caso B: fs = 15 Hz (Cumple 2*fs <= fm), Fase = pi/2 (Coseno)
    t2, y2 = f.generar_senoidal(15, fm, np.pi/2, t_i, t_f)

    # --- Graficación ---
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.stem(t1, y1)
    plt.title(f"Senoidal A: $f_s=5Hz$, $\phi=0$, $f_m=100Hz$")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.stem(t2, y2)
    plt.title(f"Senoidal B: $f_s=15Hz$, $\phi=\pi/2$, $f_m=100Hz$")
    plt.xlabel("Tiempo (s)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def main2():
    fm = 70       # Frecuencia de muestreo (Hz)
    t_i, t_f = 0, 1 # Intervalo [0, 1] segundos

    # Caso A: fs = 5 Hz (Cumple 2*fs <= fm), Fase = 0
    t1, y1 = f.generar_sync(1, fm, t_i, t_f)

    # Caso B: fs = 15 Hz (Cumple 2*fs <= fm), Fase = pi/2 (Coseno)
    t2, y2 = f.generar_sync(5, fm, t_i, t_f)

    # --- Graficación ---
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.stem(t1, y1)
    plt.title(f"Sync A: $f_s=5Hz$, $f_m=70Hz$")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.stem(t2, y2)
    plt.title(f"Sync B: $f_s=15Hz$, $f_m=70Hz$")
    plt.xlabel("Tiempo (s)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def main3():
    fm = 50       # Frecuencia de muestreo (Hz)
    t_i, t_f = 0, 1 # Intervalo [0, 1] segundos

    # Caso A: fs = 5 Hz (Cumple 2*fs <= fm), Fase = 0
    t1, y1 = f.generar_onda_cuadrada(5, fm, 0, t_i, t_f)

    # Caso B: fs = 15 Hz (Cumple 2*fs <= fm), Fase = pi/2 (Coseno)
    t2, y2 = f.generar_onda_cuadrada(15, fm, np.pi/2, t_i, t_f)

    # --- Graficación ---
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.stem(t1, y1)
    plt.title(f"Onda cuadrada A: $f_s=5Hz$, $\phi=0$, $f_m=50Hz$")
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.stem(t2, y2)
    plt.title(f"Onda cuadrada B: $f_s=15Hz$, $\phi=\pi/2$, $f_m=50Hz$")
    plt.xlabel("Tiempo (s)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__": 
    main2()