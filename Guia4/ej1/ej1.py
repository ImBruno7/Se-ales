import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3
import Guia4.funcionesG4 as fg4

def main():
    Tm = 0.001
    t, aux1 = f1.generar_senoidal(A = 1 ,fs = 10, fm = 1/Tm, phi = 0, t_inicio = 0, t_fin = 1)
    _, aux2 = f1.generar_senoidal(A = 4 ,fs = 20, fm = 1/Tm, phi = 0, t_inicio = 0, t_fin = 1)
    s = aux1+aux2
   
    frecuencias, magnitud,sTrans = fg4.procesar_y_centrar(s, fm = 1/Tm)

    plt.figure(figsize=(10, 5))

    # Graficamos todo el arreglo reordenado
    plt.stem(frecuencias, magnitud, basefmt="b-")

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
    frecuencias, S1_mag, S1_fft = fg4.procesar_y_centrar(señal = s1, fm = 1/Tm)
    axs[0].stem(frecuencias, S1_mag, basefmt="b-")
    axs[0].set_title('1. s[n] + 4 (Aparece DC gigante en 0 Hz)')
    axs[0].set_xlim(-30, 30) # Zoom para ver bien el centro
    axs[0].grid(True, linestyle=':')

    # 2do Cambio f2 = 11 Hz
    _, aux2_11 = f1.generar_senoidal(A=4, fs=11, fm=1/Tm, phi=0, t_inicio=0, t_fin=1)
    s2 = aux1 + aux2_11
    frecuencias,S2_mag,S2_fft = fg4.procesar_y_centrar(señal = s2, fm = 1/Tm)
    axs[1].stem(frecuencias, S2_mag, basefmt="b-")
    axs[1].set_title('2. f2 = 11 Hz (Picos limpios y separados)')
    axs[1].set_xlim(-30, 30)
    axs[1].grid(True, linestyle=':')

    # 3er Cambio f2 = 10.5 Hz
    _, aux2_105 = f1.generar_senoidal(A=4, fs=10.5, fm=1/Tm, phi=0, t_inicio=0, t_fin=1)
    s3 = aux1 + aux2_105
    frecuencias,S3_mag,S3_fft = fg4.procesar_y_centrar(señal = s3, fm = 1/Tm)
    axs[2].stem(frecuencias, S3_mag, basefmt="b-")
    axs[2].set_title('3. f2 = 10.5 Hz (Fuga Espectral - El pico se ensancha)')
    axs[2].set_xlim(-30, 30)
    axs[2].grid(True, linestyle=':')

    # 4to Cambio , tf = 2
    # Hay que regenerar ambas señales con t_fin = 2
    _, aux1_2s = f1.generar_senoidal(A=1, fs=10, fm=1/Tm, phi=0, t_inicio=0, t_fin=2)
    _, aux2_2s = f1.generar_senoidal(A=4, fs=10.5, fm=1/Tm, phi=0, t_inicio=0, t_fin=2)
    s4 = aux1_2s + aux2_2s
    frecuencias,S4_mag,S4_fft = fg4.procesar_y_centrar(señal = s4, fm = 1/Tm)
    
    axs[3].stem(frecuencias, S4_mag, basefmt="b-")
    axs[3].set_title('4. t = [0...2)s con f2 = 10.5 Hz')
    axs[3].set_xlim(-30, 30)
    axs[3].set_xlabel('Frecuencia (Hz)')
    axs[3].grid(True, linestyle=':')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


