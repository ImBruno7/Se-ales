import numpy as np
import matplotlib.pyplot as plt

def disenar_fir_completo(N, tipo_ventana='rectangular'):

    fm = 300  
    
    # PASO 1: Máscara en frecuencia (Ideal)
    H_ideal = np.ones(fm)
    H_ideal[48:53] = 0.0   # Atenuación en las frecuencias positivas (50 Hz)
    H_ideal[248:253] = 0.0 # Atenuación en su espejo negativo (300 - 50)

    # PASO 2: Aplicar el retardo de fase
    alpha = (N - 1) / 2
    k = np.arange(fm)
    termino_fase = np.exp(-1j * 2 * np.pi * alpha * (k / fm))
    H_retrasado = H_ideal * termino_fase

    # PASO 3: Antitransformar para obtener h_ideal[n]
    h_ideal = np.real(np.fft.ifft(H_retrasado))

    # PASO 4: Truncado (Quedarse con las primeras N muestras causales)
    h_recortado = h_ideal[:N]

    # Construcción de Ventanas
    M = N - 1
    n = np.arange(N)
    
    if tipo_ventana == 'rectangular':
        ventana = np.ones(N)
    elif tipo_ventana == 'bartlett':
        ventana = 1.0 - np.abs(2 * n - M) / M
    elif tipo_ventana == 'hann':
        ventana = 0.5 - 0.5 * np.cos(2 * np.pi * n / M)
    elif tipo_ventana == 'hamming':
        ventana = 0.54 - 0.46 * np.cos(2 * np.pi * n / M)
    elif tipo_ventana == 'blackman':
        ventana = 0.42 - 0.5 * np.cos(2 * np.pi * n / M) + 0.08 * np.cos(4 * np.pi * n / M)
    else:
        raise ValueError("Ventana no soportada.")

    # PASO 5: Respuesta al impulso definitiva
    h_final = h_recortado * ventana
    return h_final

def dB(magnitud):
    return 20 * np.log10(np.abs(magnitud) + 1e-12)

def main():
    fs = 300.0
    largos_N = [31, 61, 121]  
    ventanas = ['rectangular', 'bartlett', 'hann', 'hamming', 'blackman']
    titulos = [
        '1. Ventana Rectangular ',
        '2. Ventana Bartlett / Triangular ',
        '3. Ventana Hann ',
        '4. Ventana Hamming',
        '5. Ventana Blackman'
    ]
    
    colores = ['orange', 'blue', 'purple']

    w_eje = np.linspace(-np.pi, np.pi, 2000, endpoint=False)
    frecuencias_hz = w_eje * (fs / (2 * np.pi))
    z = np.exp(1j * w_eje)

    fig, axs = plt.subplots(5, 1, figsize=(11, 14), sharex=True)
    
    for idx, vent in enumerate(ventanas):
        ax = axs[idx]
        
        for j, N in enumerate(largos_N):
            h_filt = disenar_fir_completo(N, vent)
            
            # Sumatoria iterativa: H(z) = sumatoria de h[n] * z^(-n)
            H_filt = np.zeros_like(z, dtype=complex)
            for n_idx in range(N):
                H_filt += h_filt[n_idx] * (z**-n_idx)
            
            ax.plot(frecuencias_hz, dB(np.abs(H_filt)), color=colores[j], lw=1.8, label=f'N = {N} muestras')
            
        ax.set_title(titulos[idx], fontweight='bold', fontsize=11, color='darkblue' if idx%2==0 else 'black')
        ax.set_ylabel('Magnitud |H(f)|')
        ax.set_xlim(-fs/2, fs/2) 
        ax.grid(True, linestyle=':', alpha=0.6)
        
        ax.axvline(50, color='red', linestyle='--', alpha=0.5, lw=1.2)
        ax.axvline(-50, color='red', linestyle='--', alpha=0.5, lw=1.2)
        ax.legend(loc='upper right', fontsize=9)

    axs[4].set_xlabel('Frecuencia [Hz]')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()