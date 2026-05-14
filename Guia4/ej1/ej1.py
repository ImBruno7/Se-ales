import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3

def main():
    Tm = 0.001
    t, aux1 = f1.generar_senoidal(A = 1 ,fs = 10, fm = 1/Tm, phi = 0, t_inicio = 0, t_fin = 1)
    _, aux2 = f1.generar_senoidal(A = 4 ,fs = 20, fm = 1/Tm, phi = 0, t_inicio = 0, t_fin = 1)
    s = aux1+aux2
    sTrans = np.fft.fft(s)

    # Calculamos el módulo (magnitud) de los números complejos que devuelve la FFT
    magnitud = np.abs(sTrans)

    # Generamos el eje X (las frecuencias correspondientes a cada "k")
    N = len(s)
    frecuencias = np.fft.fftfreq(N, d=Tm)

    # --- Reordenamos para ver el espectro bilateral (completo) ---
    frecuencias_completas = np.fft.fftshift(frecuencias)
    magnitud_completa = np.fft.fftshift(magnitud)

    plt.figure(figsize=(10, 5))

    # Graficamos todo el arreglo reordenado
    plt.stem(frecuencias_completas, magnitud_completa, basefmt="b-")

    plt.title('Espectro Bilateral (Completo) de S[k]')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud |S[k]|')

    # Hacemos zoom desde -50 Hz hasta 50 Hz para ver los picos espejados
    plt.xlim(-50, 50)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.show()

    E_s = fG3.Norma(s,2)**2
    E_sTrans = (fG3.Norma(sTrans,2)**2)/len(sTrans)
    print(f"Energía en el tiempo (E_s): {E_s:.2f}")
    print(f"Energía en la frecuencia (E_sTrans): {E_sTrans:.2f}")

    # Creamos una figura grande con 4 subplots (uno para cada punto)
    fig, axs = plt.subplots(4, 1, figsize=(10, 14))

    # 1er Cambio s[n] + 4 ---
    # Tu señal 's' ya tiene aux1 y aux2(A=4), solo le sumamos el offset
    s1 = s + 4  
    S1_mag = np.abs(np.fft.fft(s1))
    axs[0].stem(frecuencias_completas, np.fft.fftshift(S1_mag), basefmt="b-")
    axs[0].set_title('1. s[n] + 4 (Aparece DC gigante en 0 Hz)')
    axs[0].set_xlim(-30, 30) # Zoom para ver bien el centro
    axs[0].grid(True, linestyle=':')

    # 2do Cambio f2 = 11 Hz
    _, aux2_11 = f1.generar_senoidal(A=4, fs=11, fm=1/Tm, phi=0, t_inicio=0, t_fin=1)
    s2 = aux1 + aux2_11
    S2_mag = np.abs(np.fft.fft(s2))
    axs[1].stem(frecuencias_completas, np.fft.fftshift(S2_mag), basefmt="b-")
    axs[1].set_title('2. f2 = 11 Hz (Picos limpios y separados)')
    axs[1].set_xlim(-30, 30)
    axs[1].grid(True, linestyle=':')

    # 3er Cambio f2 = 10.5 Hz
    _, aux2_105 = f1.generar_senoidal(A=4, fs=10.5, fm=1/Tm, phi=0, t_inicio=0, t_fin=1)
    s3 = aux1 + aux2_105
    S3_mag = np.abs(np.fft.fft(s3))
    axs[2].stem(frecuencias_completas, np.fft.fftshift(S3_mag), basefmt="b-")
    axs[2].set_title('3. f2 = 10.5 Hz (Fuga Espectral - El pico se ensancha)')
    axs[2].set_xlim(-30, 30)
    axs[2].grid(True, linestyle=':')

    # 4to Cambio , tf = 2
    # Hay que regenerar ambas señales con t_fin = 2
    _, aux1_2s = f1.generar_senoidal(A=1, fs=10, fm=1/Tm, phi=0, t_inicio=0, t_fin=2)
    _, aux2_2s = f1.generar_senoidal(A=4, fs=10.5, fm=1/Tm, phi=0, t_inicio=0, t_fin=2)
    s4 = aux1_2s + aux2_2s
    S4_mag = np.abs(np.fft.fft(s4))
    
    # Como cambió la duración, recalculamos el eje X para este gráfico
    N4 = len(s4)
    frecuencias_4 = np.fft.fftshift(np.fft.fftfreq(N4, d=Tm))
    
    axs[3].stem(frecuencias_4, np.fft.fftshift(S4_mag), basefmt="b-")
    axs[3].set_title('4. t = [0...2)s con f2 = 10.5 Hz')
    axs[3].set_xlim(-30, 30)
    axs[3].set_xlabel('Frecuencia (Hz)')
    axs[3].grid(True, linestyle=':')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


