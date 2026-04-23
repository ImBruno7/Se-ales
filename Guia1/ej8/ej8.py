import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1

def main():
    t,y = f1.generar_senoidal(fs=5, fm=1000, phi=0, t_inicio=0, t_fin=1)
    y = 8 * y
    ruido = np.array([f1.generar_un_valor_gaussiano(0, 1) for _ in range(len(y))])

    Psenial = np.dot(y,y) /len(y)
    Pruido  = np.dot(ruido,ruido) / len(ruido)

    SenialSucia = y + ruido
    SNR_lineal = Psenial / Pruido
    SNR_dB = 10 * np.log10(SNR_lineal)

    print("--- ANTES ---")
    print(f"Potencia Señal: {Psenial:.4f}")
    print(f"Potencia Ruido: {Pruido:.4f}")
    print(f"SNR Original: {SNR_dB:.2f} dB\n")

    # Despeje y cálculo de la constante para SNR = 0 dB
    # Sabemos que k = raiz(Psenial / Pruido)
    k = np.sqrt(SNR_lineal) 

    #Nuevo ruido y nueva señal sucia
    ruido_modificado = k * ruido
    Pruido_modificado = np.dot(ruido_modificado, ruido_modificado) / len(ruido_modificado)
    
    SenialSucia_Final = y + ruido_modificado

    # Verificamos que haya quedado en 0 dB
    SNR_nueva_lineal = Psenial / Pruido_modificado
    SNR_nueva_dB = 10 * np.log10(SNR_nueva_lineal)

    print("--- DESPUÉS ---")
    print(f"Constante k: {k:.4f}")
    print(f"Nueva Potencia Ruido: {Pruido_modificado:.4f}")
    print(f"Nueva SNR: {SNR_nueva_dB:.2f} dB")

    
    plt.figure(figsize=(10, 12)) 

    # Gráfico 1: Señal Original Pura
    plt.subplot(4, 1, 1)
    plt.plot(t, y, color='blue', linewidth=2)
    plt.title('1. Señal Original (Conocida)', fontweight='bold')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Gráfico 2: Ruido Original Puro
    plt.subplot(4, 1, 2)
    plt.plot(t, ruido, color='gray', alpha=0.7)
    plt.title(f'2. Ruido Aleatorio Generado (Potencia = {Pruido:.4f})', fontweight='bold')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Gráfico 3: Señal + Ruido Original
    plt.subplot(4, 1, 3)
    plt.plot(t, SenialSucia, color='orange')
    # Aca podés ver como la señal original todavía se "adivina"
    plt.title(f'3. Señal Combinada Original (SNR = {SNR_dB:.2f} dB)', fontweight='bold')
    plt.ylabel('Amplitud')
    plt.grid(True)

    #Gráfico 4: Señal + Ruido Amplificado (k) 
    plt.subplot(4, 1, 4)
    plt.plot(t, SenialSucia_Final, color='red')
    
    plt.title(f'4. Señal con Ruido Amplificado por k={k:.2f} (SNR = {SNR_nueva_dB:.2f} dB)', fontweight='bold')
    plt.xlabel('Tiempo [s]') 
    plt.ylabel('Amplitud')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


main()
    