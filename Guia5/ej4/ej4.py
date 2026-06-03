import numpy as np
import matplotlib.pyplot as plt

def H(s):
    h = (12500 * s) / (44*(s**2)+60625*s+625*(10**4))
    return h

def Euler(z,T):
    s = (1 - z**-1) / T
    return s

def Bilineal(z,T):
    s = (2 / T) * ((1 - z**-1)/(1 + z**-1))
    return s

def dB(magnitud):
    # Convierte magnitud a decibeles
    return 10 * np.log10(np.abs(magnitud))

def main():
    # valor arbitrario para la frecuencia de muestreo   
    fmtest = 15000
    ftest = np.arange(fmtest//2)
    sTest = 2j * np.pi * ftest          # s = jw = j2pif

    H_frecuencia = np.abs(H(sTest))    # H(s) -> respuesta en frecuencia
    fMax = np.argmax(H_frecuencia)      # w donde H(s) tiene máxima magnitud
    maxMag = H_frecuencia[fMax]
    indices_validos = np.where(H_frecuencia >= maxMag / np.sqrt(2))[0]
    fCorte = ftest[indices_validos[-1]]

    # fm = 4 x fc
    fm = 4 * fCorte
    T = 1 / fm
    f = np.arange(fm // 2)
    z = np.exp(2j*np.pi*f*T)            # z = e^j2*pi*f*T
    s = 2j*np.pi*f                      # s = j2*pi*f
    HEuler = H(Euler(z, T))           # H(z) mediante transformación de Euler
    HBilineal = H(Bilineal(z, T))     # H(z) mediante transformación bilineal

    #fm = 8 x fc #########
    fm2 = 8 * fCorte
    T2 = 1 / fm2
    f2 = np.arange(fm2 // 2)
    z2 = np.exp(2j*np.pi*f2*T2)         # z = e^j2pi f T
    s2 = 2j*np.pi*f2                    # s = j2*pi*f
    HEuler2 = H(Euler(z2, T2))        # H(z) mediante transformación de Euler
    HBilineal2 = H(Bilineal(z2, T2))  # H(z) mediante transformación bilineal

    ######### Graficas #########
    fig, ax = plt.subplots(3, 1, figsize=(15, 10))
    for axi in ax:
        axi.grid()

    # fc
    ax[0].plot(ftest, dB(H_frecuencia))
    ax[0].plot(fMax, dB(H_frecuencia[fMax]), 'go')
    ax[0].plot(fCorte, dB(H_frecuencia[fCorte]), 'ro')
    ax[0].set_title('Magnitud del sistema continuo (dB)')
    ax[0].set_xlabel('Frecuencia [Hz]')
    ax[0].set_ylabel('Magnitud [dB]')

    # fm = 4 x fc
    ax[1].plot(f, dB(H(s)), 'b', label='$H(s)$')
    ax[1].plot(f, dB(HEuler), 'r', label='Euler')
    ax[1].plot(f, dB(HBilineal), 'g', label='Bilineal')
    ax[1].set_title(f'Respuestas discretas con $f_m = 4 \\times f_c = {fm} Hz$')
    ax[1].set_xlabel('Frecuencia [Hz]')
    ax[1].set_ylabel('Magnitud [dB]')
    ax[1].legend()

    # fm = 8 x fc
    ax[2].plot(f2, dB(H(s2)), 'b', label='$H(s)$')
    ax[2].plot(f2, dB(HEuler2), 'r', label='Euler')
    ax[2].plot(f2, dB(HBilineal2), 'g', label='Bilineal')
    ax[2].set_title(f'Respuestas discretas con $f_m = 8 \\times f_c = {fm2} Hz$')
    ax[2].set_xlabel('Frecuencia [Hz]')
    ax[2].set_ylabel('Magnitud [dB]')
    ax[2].legend()

    plt.tight_layout()
    plt.show()

    #Gráfica enfocada
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(f, dB(H(s)), 'k-', linewidth=3, label='H(s) Ideal (Continuo)')
    ax.plot(f, dB(HEuler), 'r--', linewidth=2, label='Euler H(z)')
    ax.plot(f, dB(HBilineal), 'b-.', linewidth=2, label='Bilineal H(z)')

    # Marcamos el corte analógico original con un punto para ver quién le pega más cerca
    ax.plot(fCorte, dB(H_frecuencia[fCorte]), 'ko', markersize=8, label=f'Corte Ideal ({fCorte:.1f} Hz)')

    ax.set_title('Vista Detallada del Lóbulo Principal (Demostración de Fidelidad)', fontweight='bold')
    ax.set_xlabel('Frecuencia [Hz]')
    ax.set_ylabel('Magnitud [dB]')
    
    # Recortamos los ejes para centrar la imagen en la parte más alta de la campana
    ax.set_xlim(0, 600)
    ax.set_ylim(-15, -6) 
    
    ax.grid(True, linestyle=':')
    ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()