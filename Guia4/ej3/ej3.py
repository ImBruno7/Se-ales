import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3

def main():
    t,s1 = f1.generar_senoidal(A = 1, fs = 10, fm = 100, phi = 0, t_inicio = 0, t_fin = 1)
    tf1 = np.fft.fft(s1)
    i = 15
    N = len(tf1)
    k = np.arange(N)
    tf1Ret = tf1 * np.exp(-1j * 2 * np.pi * k * i / N)
    s1Ret = np.fft.ifft(tf1Ret)

    # --- Creación de la Gráfica ---
    plt.figure(figsize=(10, 5))

    # Graficamos la señal original gruesa y un poco transparente
    plt.plot(t, s1, label='Señal Original (10 Hz)', color='blue', linewidth=4, alpha=0.4)

    # Graficamos la señal retardada encima con línea punteada
    plt.plot(t, s1Ret, '--', label=f'Señal Retardada ({i} muestras)', color='red', linewidth=2)

    plt.title('Propiedad de Retardo Temporal de la TDF')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    
    # Hacemos zoom en los primeros 3 ciclos (0 a 0.3s) para que se vea claro
    plt.xlim(0, 0.3) 
    
    plt.legend(loc='upper right')
    plt.grid(True, linestyle=':')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
