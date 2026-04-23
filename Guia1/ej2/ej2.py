import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2

def main():
    fm = 30      # Frecuencia de muestreo (Hz)
    t_i, t_f = -1, 1 # Intervalo [0, 1] segundos

    # Caso A: fs = 5 Hz (Cumple 2*fs <= fm), Fase = 0
    t1, y1 = f1.generar_senoidal(1, fm, 0, t_i, t_f)

    t2,y2 = f2.inversion(t1,y1)

    y3=f2.rectificacion(y1)

    y4=f2.cuantizacion(y1)

    plt.figure(figsize=(12, 10))

    # 1. Señal Original
    plt.subplot(2, 2, 1)
    plt.stem(t1, y1)
    plt.title("1. Señal Original ($f_s=5Hz$)")
    plt.grid(True)
    plt.ylabel("Amplitud")

    # 2. Inversión Temporal
    # Usamos t2 porque es el eje de tiempo invertido que calculamos
    plt.subplot(2, 2, 2)
    plt.stem(t2, y2)
    plt.title(r"2. Inversión Temporal ($x[-n]$)")
    plt.grid(True)

    # 3. Rectificación
    plt.subplot(2, 2, 3)
    plt.stem(t1, y3)
    plt.title("3. Rectificación (Onda Completa)")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")

    # 4. Cuantización
    plt.subplot(2, 2, 4)
    plt.stem(t1, y4)
    plt.title("4. Cuantización (8 niveles)")
    plt.grid(True)
    plt.xlabel("Tiempo (s)")

    # Ajustamos el espaciado para que no se pisen los títulos
    plt.tight_layout()
    plt.show()
    
    #para comprobar mejor lo de cuantizacion
    # Esto nos dice cuántos niveles se usaron realmente
    print(f"Niveles detectados: {len(np.unique(y4))}")

    # Esto nos muestra cuáles son esos niveles
    print(f"Valores de amplitud: {np.unique(y4)}")

if __name__ == "__main__": 
    main()