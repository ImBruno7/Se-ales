import numpy as np
import matplotlib.pyplot as plt

def ventana_hamming(N):
    M = N - 1
    n = np.arange(N)
    return 0.54 - 0.46 * np.cos(2 * np.pi * n / M)

def mi_freqz(h, fm, num_puntos=16000):
    # Evaluamos desde 0 hasta fm/2 para ver la parte positiva clara
    f = np.linspace(-fm/2, fm/2, num_puntos, endpoint=False)
    T = 1.0 / fm
    z = np.exp(1j * 2 * np.pi * f * T)
    
    H = np.zeros_like(z, dtype=complex)
    for n in range(len(h)):
        H += h[n] * (z**-n)
    return f, H

def disenar_filtro_multibanda(N, fm):
    N_fft = int(fm)  # 16000 puntos = 1 Hz de resolución por índice
    
    # Mascara apagada (Todo Ceros)
    H_ideal = np.zeros(N_fft)
    
    # Bandas que pasan con 1
    # Banda 1: [100, 200]
    H_ideal[100:201] = 1.0 # [100,201) no incluye limite derecho
    
    # Banda 2: [1640, 3028]
    H_ideal[1640:3029] = 1.0
    
    # Banda 3: [5000, 6000] (Pendiente lineal de 0 a 1)
    puntos_pendiente = 6000 - 5000 + 1
    H_ideal[5000:6001] = np.linspace(0.0, 1.0, puntos_pendiente)
    
    # espejamos para freq negativas
    # Fórmulas de espejo: indice_negativo = fm - frecuencia_positiva
    H_ideal[(int(fm)-200):(int(fm)-100+1)] = 1.0
    H_ideal[(int(fm)-3028):(int(fm)-1640+1)] = 1.0
    
    # en el espejo (de -6000 a -5000) tiene que bajar (de 1 a 0)
    H_ideal[(int(fm)-6000):(int(fm)-5000+1)] = np.linspace(1.0, 0.0, puntos_pendiente)

    # RETARDO DE FASE (Para hacerlo causal)
    alpha = (N - 1) / 2
    k = np.arange(N_fft)
    termino_fase = np.exp(-1j * 2 * np.pi * alpha * (k / N_fft))
    
    # IFFT y TRUNCADO
    h_ideal = np.real(np.fft.ifft(H_ideal * termino_fase))
    h_recortado = h_ideal[:N] # no tiene sentido tener todos los ciclos
    
    # le hacemos la ventana
    h_final = h_recortado * ventana_hamming(N)
    
    return h_final, H_ideal

def main():
    fm = 16000.0
    N = 501  # Filtro de orden alto para respetar bien las transiciones
    
    # Obtenemos la respuesta al impulso y la máscara ideal original
    h_n, mascara_ideal = disenar_filtro_multibanda(N, fm)
    
    # Evaluamos la frecuencia de nuestro filtro real
    frec, H_complex = mi_freqz(h_n, fm)
    magnitud_lineal = np.abs(H_complex)
    
    # GRÁFICAS
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Graficamos la máscara ideal (solo la primera mitad hasta Nyquist)
    f_ideal = np.arange(int(-fm/2),int(fm/2))
    ax.plot(f_ideal, np.concatenate((mascara_ideal[int(fm/2):],mascara_ideal[:int(fm/2)])), color='gray', linestyle='--', 
            linewidth=2, label='Máscara Ideal Exigida')
    
    # Graficamos lo que realmente logramos con nuestro filtro
    ax.plot(frec, magnitud_lineal, color='blue', linewidth=2, 
            label=f'Filtro FIR Real (N={N}, Hamming)')
    
    ax.set_title('Filtro FIR Multibanda (Diseño por Método de Ventanas)', fontweight='bold', fontsize=14)
    ax.set_xlabel('Frecuencia [Hz]', fontsize=12)
    ax.set_ylabel('Magnitud Lineal |H(f)|', fontsize=12)
    ax.set_xlim(-fm/2, fm/2)
    ax.set_ylim(-0.1, 1.2)
    ax.grid(True, linestyle=':', alpha=0.7)
    
    # Sombreamos las bandas de interés para que quede profesional
    ax.axvspan(100, 200, color='green', alpha=0.1, label='Banda 1')
    ax.axvspan(-100, -200, color='green', alpha=0.1)

    ax.axvspan(1640, 3028, color='brown', alpha=0.1, label='Banda 2')
    ax.axvspan(-1640, -3028, color='brown', alpha=0.1)

    ax.axvspan(5000, 6000, color='purple', alpha=0.1, label='Banda 3 (Pendiente)')
    ax.axvspan(-5000, -6000, color='purple', alpha=0.1)
    
    ax.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()