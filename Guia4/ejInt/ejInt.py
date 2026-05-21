import numpy as np
import matplotlib.pyplot as plt
import Guia4.funcionesG4 as fg4
import Guia1.ej1.funciones as f1

def main():
    # PARTE I: Señal Original y Aliasing
    fm1 = 1000                                          # Frecuencia de muestreo 1
    t, s1 = f1.generar_senoidal(A=5, fs=50, fm=fm1, phi=0, t_inicio=0, t_fin=1)
    _, s2 = f1.generar_senoidal(A=3, fs=120, fm=fm1, phi=0, t_inicio=0, t_fin=1)
    _, s3 = f1.generar_senoidal(A=2, fs=280, fm=fm1, phi=0, t_inicio=0, t_fin=1)

    signal = s1 + s2 + s3                               # Señal combinada sin randoms
    N1 = len(signal)
    
    f_centradas1, mag1, S_k1 = fg4.procesar_y_centrar(señal=signal, fm=fm1)
    delta_f1 = fm1 / N1                                 # Resolución frecuencial = 1 Hz

    # Submuestreo a fm = 200 Hz
    fm2 = 200
    _, s1_200 = f1.generar_senoidal(A=5, fs=50, fm=fm2, phi=0, t_inicio=0, t_fin=1)
    _, s2_200 = f1.generar_senoidal(A=3, fs=120, fm=fm2, phi=0, t_inicio=0, t_fin=1)
    _, s3_200 = f1.generar_senoidal(A=2, fs=280, fm=fm2, phi=0, t_inicio=0, t_fin=1)
    
    signal_200 = s1_200 + s2_200 + s3_200
    f_centradas2, mag2, _ = fg4.procesar_y_centrar(señal=signal_200, fm=fm2)

    # Gráficas Parte I (Con stem y marcas numéricas claras)
    fig, axs = plt.subplots(2, 1, figsize=(11, 7))
    axs[0].stem(f_centradas1, mag1, linefmt='b-', markerfmt='bo', basefmt='k-')
    axs[0].set_title(f'Espectro original (fm=1000Hz, Δf={delta_f1}Hz)')
    axs[0].set_xlim(-350, 350)
    axs[0].set_xticks([-280, -120, -50, 0, 50, 120, 280]) # Números exactos de los picos
    axs[0].grid(True, linestyle=':')
    
    axs[1].stem(f_centradas2, mag2, linefmt='r-', markerfmt='ro', basefmt='k-')
    axs[1].set_title('Espectro con Aliasing (fm=200Hz)')
    axs[1].set_xlim(-110, 110)
    axs[1].set_xticks([-80, -50, 0, 50, 80])             # Números exactos del aliasing
    axs[1].grid(True, linestyle=':')
    plt.tight_layout()

    # PARTE II: Resolución temporal y Zero-Padding (Dibujos separados)
    t_corta, s1_c = f1.generar_senoidal(A=5, fs=50, fm=fm1, phi=0, t_inicio=0, t_fin=0.04)
    _, s2_c = f1.generar_senoidal(A=3, fs=120, fm=fm1, phi=0, t_inicio=0, t_fin=0.04)
    _, s3_c = f1.generar_senoidal(A=2, fs=280, fm=fm1, phi=0, t_inicio=0, t_fin=0.04)
    sig_corta = s1_c + s2_c + s3_c
    N_corta = len(sig_corta)
    delta_f_corta = fm1 / N_corta                       # Resolución = 25 Hz

    S_k_corta = np.fft.fft(sig_corta)
    S_c_centrado = np.concatenate((S_k_corta[N_corta//2:], S_k_corta[:N_corta//2]))
    f_c_centradas = np.arange(-N_corta//2, N_corta - N_corta//2) * delta_f_corta

    # Zero-Padding a 5N
    sig_pad = np.zeros(5 * N_corta)
    sig_pad[:N_corta] = sig_corta
    N_pad = len(sig_pad)
    
    S_k_pad = np.fft.fft(sig_pad)
    S_pad_centrado = np.concatenate((S_k_pad[N_pad//2:], S_k_pad[:N_pad//2]))
    f_pad_centradas = np.arange(-N_pad//2, N_pad - N_pad//2) * (fm1 / N_pad)

    # Gráficas Parte II: Dos subplots separados lado a lado (1 fila, 2 columnas)
    fig2, axs2 = plt.subplots(1, 2, figsize=(14, 4))
    
    # Lado izquierdo: Señal de 40ms pura
    axs2[0].stem(f_c_centradas, np.abs(S_c_centrado), linefmt='orange', markerfmt='og', basefmt='k-')
    axs2[0].set_title('Original Corta (40ms, Δf=25Hz)')
    axs2[0].set_xlim(-200, 200)
    axs2[0].set_xticks([-150, -100, -50, 0, 50, 100, 150])
    axs2[0].grid(True, linestyle=':')
    
    # Lado derecho: Señal con Zero-Padding
    axs2[1].stem(f_pad_centradas, np.abs(S_pad_centrado), linefmt='purple', markerfmt='m.', basefmt='k-')
    axs2[1].set_title('Con Zero-Padding (Longitud 5N)')
    axs2[1].set_xlim(-200, 200)
    axs2[1].set_xticks([-120, -50, 0, 50, 120])
    axs2[1].grid(True, linestyle=':')
    plt.tight_layout()

    # PARTE III: Linealidad y Teorema de Parseval

    _, x1 = f1.generar_senoidal(A=5, fs=50, fm=fm1, phi=0, t_inicio=0, t_fin=1)
    _, x2 = f1.generar_senoidal(A=3, fs=120, fm=fm1, phi=np.pi/2, t_inicio=0, t_fin=1) # Desfase para coseno
    _, x3 = f1.generar_senoidal(A=2, fs=280, fm=fm1, phi=0, t_inicio=0, t_fin=1)
    x_total = x1 + x2 + x3

    X1_k = np.fft.fft(x1)
    X2_k = np.fft.fft(x2)
    X3_k = np.fft.fft(x3)
    X_total_k = np.fft.fft(x_total)
    
    print(f"Error de linealidad: {np.max(np.abs(X_total_k - (X1_k + X2_k + X3_k))):.15f}")

    E_tiempo = np.sum(x_total**2)
    E_frecuencia = np.sum(np.abs(X_total_k)**2) / N1
    print(f"Energía Tiempo: {E_tiempo:.2f} | Energía Frecuencia: {E_frecuencia:.2f}\n")

    # GRÁFICAS PARTE III: Verificación de Linealidad (4 gráficos)
    # Centramos los 4 espectros complejos para que coincidan con el eje de frecuencias
    X1_centrado = np.concatenate((X1_k[N1//2:], X1_k[:N1//2]))
    X2_centrado = np.concatenate((X2_k[N1//2:], X2_k[:N1//2]))
    X3_centrado = np.concatenate((X3_k[N1//2:], X3_k[:N1//2]))
    X_tot_centrado = np.concatenate((X_total_k[N1//2:], X_total_k[:N1//2]))

    fig4, axs4 = plt.subplots(4, 1, figsize=(11, 9), sharex=True)
    fig4.suptitle('Verificación Gráfica de la Propiedad de Linealidad', fontsize=14, fontweight='bold')

    # Gráfico 1: Componente 1 (50 Hz)
    axs4[0].stem(f_centradas1, np.abs(X1_centrado), linefmt='c-', markerfmt='co', basefmt='k-')
    axs4[0].set_title('Espectro Individual |X1[k]| (50 Hz)')
    axs4[0].grid(True, linestyle=':')

    # Gráfico 2: Componente 2 (120 Hz)
    axs4[1].stem(f_centradas1, np.abs(X2_centrado), linefmt='m-', markerfmt='mo', basefmt='k-')
    axs4[1].set_title('Espectro Individual |X2[k]| (120 Hz)')
    axs4[1].grid(True, linestyle=':')

    # Gráfico 3: Componente 3 (280 Hz)
    axs4[2].stem(f_centradas1, np.abs(X3_centrado), linefmt='y-', markerfmt='yo', basefmt='k-')
    axs4[2].set_title('Espectro Individual |X3[k]| (280 Hz)')
    axs4[2].grid(True, linestyle=':')

    # Gráfico 4: Señal Suma Total
    axs4[3].stem(f_centradas1, np.abs(X_tot_centrado), linefmt='k-', markerfmt='ko', basefmt='k-')
    axs4[3].set_title('Espectro de la Señal Combinada Total |X[k]| = |X1[k] + X2[k] + X3[k]|')
    axs4[3].set_xlabel('Frecuencia [Hz]')
    axs4[3].set_xlim(-350, 350)
    axs4[3].set_xticks([-280, -120, -50, 0, 50, 120, 280]) # Marcas numéricas claras en todas las componentes
    axs4[3].grid(True, linestyle=':')
    plt.tight_layout()

    # PARTE IV: Filtro Ideal en Frecuencia
    S_centrado_complejo = np.concatenate((S_k1[N1//2:], S_k1[:N1//2]))

    # Máscara Pasa-Bajos Ideal (Corte en 200 Hz)
    H_k = np.where(np.abs(f_centradas1) <= 200, 1.0, 0.0)
    S_filtrado_centrado = S_centrado_complejo * H_k

    S_k_filtrada_cruda = np.concatenate((S_filtrado_centrado[N1//2:], S_filtrado_centrado[:N1//2]))
    y_n = np.real(np.fft.ifft(S_k_filtrada_cruda))

    # Gráficas Parte IV (Con stem en las magnitudes de frecuencia)
    fig3, axs3 = plt.subplots(3, 1, figsize=(11, 8))
    axs3[0].stem(f_centradas1, H_k, linefmt='m-', markerfmt='mo', basefmt='k-')
    axs3[0].set_title('Respuesta en Frecuencia del Filtro H[k] (Corte en 200 Hz)')
    axs3[0].set_xticks([-200, 0, 200])
    axs3[0].grid(True, linestyle=':')
    
    axs3[1].stem(f_centradas1, np.abs(S_filtrado_centrado), linefmt='g-', markerfmt='go', basefmt='k-')
    axs3[1].set_title('Espectro de Magnitud Filtrado (280 Hz Eliminada)')
    axs3[1].set_xlim(-350, 350)
    axs3[1].set_xticks([-120, -50, 0, 50, 120])          # Ya no aparece la marca del 280
    axs3[1].grid(True, linestyle=':')
    
    axs3[2].plot(t, signal, color='blue', alpha=0.4, label='Original x[n]', linewidth=2)
    axs3[2].plot(t, y_n, color='green', label='Filtrada y[n]', linewidth=1.5)
    axs3[2].set_title('Comparativa en el Tiempo (Zoom 0 a 0.1s)')
    axs3[2].set_xlim(0, 0.1)
    axs3[2].grid(True, linestyle=':')
    axs3[2].legend()
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()