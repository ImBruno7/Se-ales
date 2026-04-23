import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1

def main():

    t, y = f1.generar_senoidal(fs=4000, fm=129, phi=0, t_inicio=0, t_fin=2)

    # --- Graficación del Experimento de Nyquist (fm > 2 * fmax) ---
    plt.figure(figsize=(15, 12))

    # Graficamos con stem para ver los puntos reales de muestreo
    plt.stem(t, y, linefmt='C0-', markerfmt='C0o', basefmt='black')
    # Agregamos un plot suave de fondo para ver qué "forma" parece tener
    plt.plot(t, y, 'r--', alpha=0.3) 
    plt.ylim(-1.2, 1.2)
    plt.title(f"Fm = 129   Hz (fs=4000 Hz)")
    plt.grid(True, alpha=0.3)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")

    plt.tight_layout()
    plt.show()



main()


#Cuando muestreamos a una frecuencia f_m, cualquier frecuencia f_s se verá como una frecuencia aparente (f_a) 
#según esta relación:
#f_a = |f_s - k * f_m|
