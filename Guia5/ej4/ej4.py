import numpy as np
import matplotlib.pyplot as plt

def H(s):
    h = (12500 * s) / (44*(s**2)+60625*s+625*(10**4))
    return h

def euler(z,T):
    s = (1 - z**-1) / T
    return s

def bilineal(z,T):
    s = (2 / T) * ((1 - z**-1)/(1 + z**-1))
    return s

def main():
    # PARTE 1: Determinar la frecuencia de corte y de muestreo
    f_test = np.linspace(1, 1000, 50000)
    s_test = 1j * 2 * np.pi * f_test
    mag_test = np.abs(H(s_test))

    # Buscamos el pico máximo y calculamos el umbral de caída de -3dB (dividir por raíz de 2)
    mag_max = np.max(mag_test)
    mag_3db = mag_max / np.sqrt(2)

    # Filtramos dónde la gráfica está por encima de los -3dB
    indices_3db = np.where(mag_test >= mag_3db)[0]
    fc1 = f_test[indices_3db[0]]   # La primera vez que cruza el umbral (corte inferior)
    fc2 = f_test[indices_3db[-1]]  # La última vez que cruza el umbral (corte superior)

    # Usamos fc2 para evitar el aliasing de la banda más alta.
    fm = 4 * fc2
    T = 1 / fm

    # Imprimimos los resultados en la consola para el profe
    print("--- RESULTADOS PARTE 1 ---")
    print(f"Frecuencia de corte inferior (fc1): {fc1:.2f} Hz")
    print(f"Frecuencia de corte superior (fc2): {fc2:.2f} Hz")
    print(f"Frecuencia de muestreo calculada (fm = 4*fc2): {fm:.2f} Hz")
    print(f"Periodo de muestreo (T): {T:.6f} s\n")

    # PARTE 2: Análisis de respuesta en frecuencia
    f = np.linspace(0.1, fm/2, 1000) #(desde casi 0 hasta Nyquist: fm/2)

    # A. Analógico Original
    s_analogico = 1j * 2 * np.pi * f
    H_analog = H(s_analogico)
    mag_analog_db = 20 * np.log10(np.abs(H_analog))

    # B. Discretos (Mapeo a Z)
    z = np.exp(1j * 2 * np.pi * f / fm)

    s_eu = euler(z, T)
    H_euler = H(s_eu)
    mag_euler_db = 20 * np.log10(np.abs(H_euler))

    s_bil = bilineal(z, T)
    H_bilineal = H(s_bil)
    mag_bilineal_db = 20 * np.log10(np.abs(H_bilineal))

    #grafica
    fig, ax = plt.subplots(figsize=(11, 5))
    
    ax.plot(f, mag_analog_db, color='black', linewidth=3, label='Analógico Original H(s)')
    ax.plot(f, mag_euler_db, color='red', linestyle='--', linewidth=2, label='Euler H(z)')
    ax.plot(f, mag_bilineal_db, color='blue', linestyle='-.', linewidth=2, label='Bilineal H(z)')

    # Línea vertical para marcar visualmente el corte y notar el desfase
    ax.axvline(fc2, color='gray', linestyle=':', linewidth=2, label=f'Corte Superior Analógico ({fc2:.1f} Hz)')

    ax.set_title(f'Comparación de Transformaciones (fm = {fm:.1f} Hz)', fontweight='bold')
    ax.set_xlabel('Frecuencia [Hz]')
    ax.set_ylabel('Magnitud [dB]')
    ax.set_xlim(0, fm/2)
    ax.set_ylim(-40, 5)  # Acotamos para que se vea claro el detalle del pico
    ax.grid(True, linestyle=':')
    ax.legend(loc='lower left')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()