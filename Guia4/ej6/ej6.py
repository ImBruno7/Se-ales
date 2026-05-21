import numpy as np
import matplotlib.pyplot as plt
import Guia4.funcionesG4 as fg4
import Guia1.ej1.funciones as f1

def main():
    fm = 360                                  
    
    s = np.loadtxt('Guia4/necg.txt')                
    N = len(s)
    t = np.arange(N) / fm                        # Vector de tiempo real
    
    # Transformada de Fourier
    f_centradas, magnitud, S_k = fg4.procesar_y_centrar(señal = s, fm = 360)
    S_k = np.concatenate((S_k[N//2:], S_k[:N//2]))
    # Filtrado en Frecuencia
    # Buscamos los índices del ruido usando valor absoluto (para agarrar positivas y negativas)
    indices_ruido = (np.abs(f_centradas) >= 40) & (np.abs(f_centradas) <= 180)
    
    S_k_filtrada = S_k.copy()
    S_k_filtrada[indices_ruido] = 0              # Hacemos cero el ruido de 40 a 180 Hz

    # volvemos a aplicar el concatenate para dejarlo en el orden que exige la ifft
    S_k_filtrada = np.concatenate(( S_k_filtrada[N//2:],  S_k_filtrada[:N//2]))
    # Retorno al dominio del Tiempo
    s_filtrada = np.real(np.fft.ifft(S_k_filtrada)) # Antitransformada limpia

    # --- Gráficas ---
    fig, axs = plt.subplots(2, 1, figsize=(12, 7))
    
    # Gráfica de la señal original ruidosa
    axs[0].plot(t, s, color='red', alpha=0.7, linewidth=0.8)
    axs[0].set_title('Señal de ECG Original (Contaminada con ruido)')
    axs[0].set_ylabel('Amplitud')
    axs[0].grid(True, linestyle=':')
    
    # Gráfica de la señal limpia
    axs[1].plot(t, s_filtrada, color='green', linewidth=1.2)
    axs[1].set_title('Señal de ECG Filtrada (Ruido de 40-180 Hz eliminado)')
    axs[1].set_xlabel('Tiempo [s]')
    axs[1].set_ylabel('Amplitud')
    axs[1].grid(True, linestyle=':')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()


    