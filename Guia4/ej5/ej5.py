import numpy as np
import matplotlib.pyplot as plt
import Guia4.funcionesG4 as fg4
import Guia1.ej1.funciones as f1

def main():
    t,s = f1.generar_senoidal(A=2, fs=27, fm=50, phi=0, t_inicio=0, t_fin=1)
    f_centradas, mag1, S_k = fg4.procesar_y_centrar(s, fm=50)
    _,s2 = f1.generar_senoidal(A=1, fs=105, fm=50, phi=0, t_inicio=0, t_fin=1)
    f_centradas, mag2, S_k = fg4.procesar_y_centrar(s2, fm=50)

   # --- Gráficos ---
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))
    plt.subplots_adjust(hspace=0.4)

    # Gráfico Caso 1
    axs[0].stem(f_centradas, mag1, linefmt='b-', markerfmt='bo', basefmt='r-')
    axs[0].set_title(f"Espectro para fs = 27 Hz (Muestreado a 50 Hz)")
    axs[0].set_xlabel("Frecuencia [Hz]")
    axs[0].set_ylabel("Magnitud |S[k]|")
    axs[0].grid(True, alpha=0.3)

    # Gráfico Caso 2
    
    axs[1].stem(f_centradas, mag2, linefmt='g-', markerfmt='go', basefmt='r-')
    axs[1].set_title(f"Espectro para fs = 105 Hz (Muestreado a 50 Hz))")
    axs[1].set_xlabel("Índice k (Frecuencia [Hz])")
    axs[1].set_ylabel("Magnitud |S[k]|")
    axs[1].grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()