import numpy as np
import matplotlib.pyplot as plt
import Guia4.funcionesG4 as fg4

def main():
    fm = 1000 
    t_inicio = -1
    t_fin = 1
    N = int((t_fin - t_inicio) * fm)
    t = np.arange(N) / fm + t_inicio

    ancho_a = 0.5 
    vent_ancha = np.where(np.abs(t) <= ancho_a / 2, 1.0, 0.0)

    ancho_b = 0.05
    vent_angosta = np.where(np.abs(t) <= ancho_b / 2, 1.0, 0.0)

    impulso = np.zeros(N)
    impulso[np.argmin(np.abs(t))] = 1.0 

    # Ignoramos f_centradas y S_k con '_', nos quedamos solo con magnitud
    frecuencias, F_ancha, _ = fg4.procesar_y_centrar(vent_ancha, fm)     # Magnitud ventana ancha
    _, F_angosta, _ = fg4.procesar_y_centrar(vent_angosta, fm) # Magnitud ventana angosta
    _, F_impulso, _ = fg4.procesar_y_centrar(impulso, fm)      # Magnitud del impulso

    fig, axs = plt.subplots(3, 2, figsize=(14, 10))
    fig.suptitle('Relación de Dispersión Tiempo-Frecuencia', fontsize=14, fontweight='bold')

    axs[0, 0].plot(t, vent_ancha, 'b', linewidth=3)
    axs[0, 0].set_title('Tiempo: Ventana Ancha')
    axs[0, 0].set_xlim(-0.6, 0.6)
    axs[0, 0].grid(True, linestyle=':')

    axs[0, 1].plot(frecuencias, F_ancha, 'b', linewidth=2)
    axs[0, 1].set_title('Frecuencia: Espectro Angosto')
    axs[0, 1].set_xlim(-60, 60)
    axs[0, 1].grid(True, linestyle=':')

    axs[1, 0].plot(t, vent_angosta, 'r', linewidth=3)
    axs[1, 0].set_title('Tiempo: Ventana Angosta')
    axs[1, 0].set_xlim(-0.6, 0.6)
    axs[1, 0].grid(True, linestyle=':')

    axs[1, 1].plot(frecuencias, F_angosta, 'r', linewidth=2)
    axs[1, 1].set_title('Frecuencia: Espectro Ancho')
    axs[1, 1].set_xlim(-60, 60)
    axs[1, 1].grid(True, linestyle=':')

    axs[2, 0].stem(t, impulso, basefmt="k-", linefmt='g-', markerfmt='go')
    axs[2, 0].set_title('Tiempo: Impulso de Dirac')
    axs[2, 0].set_xlim(-0.1, 0.1)
    axs[2, 0].grid(True, linestyle=':')

    axs[2, 1].plot(frecuencias, F_impulso, 'g', linewidth=2)
    axs[2, 1].set_title('Frecuencia: Espectro Plano')
    axs[2, 1].set_xlim(-60, 60)
    axs[2, 1].grid(True, linestyle=':')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()