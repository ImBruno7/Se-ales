import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1

def main():

    t1, y1 = f1.generar_senoidal(fs=5, fm=100, phi=0, t_inicio=0, t_fin=1)
    t2, y2 = f1.generar_senoidal(fs=5, fm=25, phi=0, t_inicio=0, t_fin=1)
    t3, y3 = f1.generar_senoidal(fs=5, fm=10, phi=0, t_inicio=0, t_fin=1)
    t4, y4 = f1.generar_senoidal(fs=5, fm=4, phi=0, t_inicio=0, t_fin=1)
    t5, y5 = f1.generar_senoidal(fs=5, fm=1, phi=0, t_inicio=0, t_fin=1)
    t6, y6 = f1.generar_senoidal(fs=5, fm=0.5, phi=0, t_inicio=0, t_fin=1)

    # --- Graficación del Experimento de Nyquist (fm > 2 * fmax) ---
    plt.figure(figsize=(15, 12))
    
    config = [
        (t1, y1, 100), (t2, y2, 25), (t3, y3, 10),
        (t4, y4, 4),   (t5, y5, 1),  (t6, y6, 0.5)
    ]

    for i, (t, y, fm) in enumerate(config, 1):
        plt.subplot(3, 2, i)
        # Graficamos con stem para ver los puntos reales de muestreo
        plt.stem(t, y, linefmt='C0-', markerfmt='C0o', basefmt='black')
        # Agregamos un plot suave de fondo para ver qué "forma" parece tener
        plt.plot(t, y, 'r--', alpha=0.3) 
        plt.ylim(-1.2, 1.2)
        plt.title(f"Fm = {fm} Hz (fs=5 Hz)")
        plt.grid(True, alpha=0.3)
        if i > 4: plt.xlabel("Tiempo [s]")
        if i % 2 != 0: plt.ylabel("Amplitud")

    plt.tight_layout()
    plt.show()


main()