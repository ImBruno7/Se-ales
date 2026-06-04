import numpy as np
import matplotlib.pyplot as plt

def to_dB(magnitud):
    return 20 * np.log10(np.abs(magnitud) + 1e-12)

def main():
    
    #PARTE 1

    #  coeficientes de H(z) = (1*z^2 + 0.5*z + 0) / (1*z^2 - 0.8*z + 0.12)
    coef_numerador = [1, 0.5, 0]
    coef_denominador = [1, -0.8, 0.12]

    # raices
    ceros = np.roots(coef_numerador)
    polos = np.roots(coef_denominador)

    print("Ceros calculados por Python:", ceros)
    print("Polos calculados por Python:", polos)

    # gráfica del Plano Z
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujamos el Círculo Unitario (límite de estabilidad)
    circulo = plt.Circle((0, 0), 1, color='gray', fill=False, linestyle='--', lw=2)
    ax.add_artist(circulo)
    
    # Ejes coordenados que cruzan por el (0,0)
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    
    # Graficamos Ceros (círculos azules) y Polos (cruces rojas)
    ax.plot(np.real(ceros), np.imag(ceros), 'bo', markersize=9, fillstyle='none', mew=2, label='Ceros')
    ax.plot(np.real(polos), np.imag(polos), 'rx', markersize=10, mew=2, label='Polos')
    
    # Detalles estéticos para el informe
    ax.set_title('Mapa de Polos y Ceros en el Plano Z', fontweight='bold')
    ax.set_xlabel('Eje Real')
    ax.set_ylabel('Eje Imaginario')
    
    # Acotamos los ejes para que el círculo se vea bien redondo
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal') # Fuerza a que la escala X e Y sean idénticas
    ax.grid(True, linestyle=':')
    ax.legend(loc='upper right')

    plt.tight_layout()
    plt.show()
    
    #PARTE 2
    fm = 1000.0  
    T = 1.0 / fm
    
   #respuesta en frecuencia
    frec_hz = np.linspace(0, fm/2, 1000, endpoint=False)
    
    # Evaluamos en el círculo unitario: z = e^(j*w)
    z = np.exp(1j * 2 * np.pi * frec_hz * T)
    
    # Función de transferencia H(z)
    H_z = (z**2 + 0.5*z) / (z**2 - 0.8*z + 0.12)
    
    magnitud_db = to_dB(H_z)
    fase_rad = np.angle(H_z)

    # respuesta al impulso
    N_muestras = 30
    n_vector = np.arange(N_muestras)
    
    # Entrada x[n]: Impulso en cero
    x = np.zeros(N_muestras)
    x[0] = 1.0
    
    # Salida h[n] (y[n] cuando la entrada es un impulso)
    h_n = np.zeros(N_muestras)
    
    for n in range(N_muestras):
        x_n = x[n]
        x_n1 = x[n-1] if n-1 >= 0 else 0.0
        
        y_n1 = h_n[n-1] if n-1 >= 0 else 0.0
        y_n2 = h_n[n-2] if n-2 >= 0 else 0.0
        
        h_n[n] = x_n + 0.5 * x_n1 + 0.8 * y_n1 - 0.12 * y_n2

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(11, 13))

    # --- Gráfico A: Magnitud ---
    ax1.plot(frec_hz, magnitud_db, 'b-', lw=2)
    ax1.set_title('Magnitud de la Respuesta en Frecuencia (Filtro Pasa-Bajos)', fontweight='bold', fontsize=12)
    ax1.set_ylabel('Magnitud [dB]')
    ax1.grid(True, linestyle=':')
    
    # Doble eje X (Hz arriba, Normalizada abajo)
    ax1_norm = ax1.secondary_xaxis('top', functions=(lambda x: x/fm, lambda x: x*fm))
    ax1_norm.set_xlabel('Frecuencia Normalizada ($f/f_m$)', color='darkblue')

    # --- Gráfico B: Fase ---
    ax2.plot(frec_hz, fase_rad, 'r-', lw=2)
    ax2.set_title('Fase de la Respuesta en Frecuencia', fontweight='bold', fontsize=12)
    ax2.set_xlabel('Frecuencia [Hz]')
    ax2.set_ylabel('Fase [Radianes]')
    ax2.grid(True, linestyle=':')

    # --- Gráfico C: Impulso ---
    ax3.stem(n_vector, h_n, linefmt='g-', markerfmt='go', basefmt='k-')
    ax3.set_title('Respuesta al Impulso h[n] (Calculada por Ecuación de Diferencias)', fontweight='bold', fontsize=12)
    ax3.set_xlabel('Muestras ($n$)')
    ax3.set_ylabel('Amplitud')
    ax3.set_xticks(np.arange(0, N_muestras, 2))
    ax3.grid(True, linestyle=':')

    # Ajuste de espacios para que no se superpongan los ejes con los títulos
    plt.tight_layout(pad=3.0, h_pad=4.0)
    plt.show()

    #PARTE 3 y PARTE 4
    # Parámetros del sistema
    T = 0.1
    fm = 1 / T          # 10 Hz
    f_nyquist = fm / 2  # 5 Hz
    
    # Eje de frecuencias para evaluar
    frec_hz = np.linspace(0.0, f_nyquist, 1000)
    
    # EVALUACIÓN DEL SISTEMA ANALÓGICO H_a(s)
    w_analogica = 2 * np.pi * frec_hz
    s = 1j * w_analogica
    H_analogico = 1 / (s + 1)
    
    # EVALUACIÓN DE SISTEMAS DISCRETOS H(z)
    # Evaluamos en el círculo unitario z = e^(j * w * T)
    z = np.exp(1j * 2 * np.pi * frec_hz * T)
    
    # La ecuación de Euler Atrasado (Parte III)
    H_euler = 1 / (11 - 10 * z**-1)
    
    # La ecuación Bilineal (Parte IV)
    H_bilineal = (1 + z**-1) / (21 - 19 * z**-1)
    
    #GRAFICA
    fig, ax = plt.subplots(figsize=(11, 7))
    
    # Graficamos las tres magnitudes en dB
    ax.plot(frec_hz, to_dB(H_analogico), 'k-', linewidth=3.5, label='Filtro Analógico Ideal H_a(s)')
    ax.plot(frec_hz, to_dB(H_euler), 'r--', linewidth=2.5, label='Aproximación Discreta (Euler)')
    ax.plot(frec_hz, to_dB(H_bilineal), 'b-.', linewidth=2.5, label='Aproximación Discreta (Bilineal)')
    
    ax.set_title(f'Partes III y IV: Comparativa Analógico vs. Euler vs. Bilineal (T={T}s)', fontweight='bold', fontsize=14)
    ax.set_xlabel('Frecuencia [Hz]', fontsize=12)
    ax.set_ylabel('Magnitud [dB]', fontsize=12)
    
    # Límites lógicos (vamos desde 0 hasta la frecuencia de Nyquist)
    ax.set_xlim(0, f_nyquist)
    ax.set_ylim(-35, 5) # Ampliamos un poco el piso para ver bien las caídas
    
    # Marcamos la frecuencia de Nyquist con una línea punteada
    ax.axvline(f_nyquist, color='gray', linestyle=':', label='Límite de Nyquist (5 Hz)')
    
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.legend(loc='lower left', fontsize=11)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()