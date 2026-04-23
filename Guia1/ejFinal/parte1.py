import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2

def main():
    #parte 1
    t,y = f1.generar_senoidal(fs = 10, fm = 400, phi=np.pi / 4, t_inicio=0, t_fin = 1)
    y = 5 * y #amplitud
    yrectificada = f2.rectificacion(yn = y,type = "onda_completa")
    ycuantizada = f2.cuantizacion(yn = yrectificada,N = 16)

    graficos1(t=t,y=y,yrectificada=yrectificada,ycuantizada=ycuantizada)

    #PARTE 2
    ruido1 = f1.generar_ruido(len(y),0,1)
    ruido2 = f1.generar_ruido(len(y),0,5)
   
    Ysucia1 = ycuantizada + ruido1
    Ysucia2 = ycuantizada + ruido2
    
    Pr1 = np.dot(ruido1,ruido1)/len(ruido1)
    Pr2 = np.dot(ruido2,ruido2)/len(ruido2)
    Ps = np.dot(ycuantizada,ycuantizada)/len(y)

    graficos2(t,ycuantizada,Ysucia1,Ysucia2,Pr1,Pr2,Ps)

    #Cálculo de la constante k para SNR = 6 dB 
    # SNR_dB = 10 * log10(Ps / Pn_final) -> 6 = 10 * log10(Ps / (k^2 * Pr1))
    snr_lineal_objetivo = 10**(6/10) # 10^0.6 ≈ 3.98
    k1 = np.sqrt(Ps / (snr_lineal_objetivo * Pr1))
    k2 = np.sqrt(Ps / (snr_lineal_objetivo * Pr2))

    ruido1_modificado = k1 * ruido1
    ruido2_modificado = k2 * ruido2

    # nuevas potencias de ruido
    Pr1_modificada = np.dot(ruido1_modificado, ruido1_modificado) / len(ruido1_modificado)
    Pr2_modificada = np.dot(ruido2_modificado, ruido2_modificado) / len(ruido2_modificado)

    # nuevas SNR en dB para verificar
    SNR1_final_dB = 10 * np.log10(Ps / Pr1_modificada)
    SNR2_final_dB = 10 * np.log10(Ps / Pr2_modificada)

    print("--- RESULTADOS SNR = 6 dB ---")
    print("CASO 1 (Ruido original varianza baja):")
    print(f"  > Constante k1 aplicada : {k1:.4f}")
    print(f"  > SNR resultante        : {SNR1_final_dB:.2f} dB\n")

    print("CASO 2 (Ruido original varianza alta):")
    print(f"  > Constante k2 aplicada : {k2:.4f}")
    print(f"  > SNR resultante        : {SNR2_final_dB:.2f} dB")






def graficos1(t,y,yrectificada,ycuantizada):
    # Gráficos de la Parte I
    plt.figure(figsize=(12, 8))

    # --- Subplot 1: Señal Original ---
    plt.subplot(2, 1, 1)
    plt.plot(t, y, color='blue', linewidth=1.5)
    plt.title('Señal Original (Senoidal Discreta)', fontweight='bold')
    plt.ylabel('Amplitud')
    plt.grid(True)
    # Acotamos un poco el eje X para que se vean bien los ciclos (ej: primeros 0.3 segundos)
    plt.xlim(0, 0.3) 

    # --- Subplot 2: Señal Rectificada y Cuantizada superpuesta con la original ---
    plt.subplot(2, 1, 2)
    # Dibujamos la original de fondo clarita para comparar
    plt.plot(t, y, color='blue', linestyle='dashed', alpha=0.3, label='Original') 
    
    # Dibujamos la cuantizada. El parámetro drawstyle='steps-mid' es CLAVE 
    # para visualizar el efecto "escalera" de la cuantización
    plt.plot(t, ycuantizada, color='red', drawstyle='steps-mid', linewidth=2, label='Rectificada y Cuantizada')
    
    plt.title('Efecto de la Rectificación y Discretización en Amplitud (N=16)', fontweight='bold')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, 0.3) # Mismo zoom que arriba

    plt.tight_layout()
    plt.show()

def graficos2(t,ycuantizada,Ysucia1,Ysucia2,Pr1,Pr2,Py):

    plt.figure(figsize=(12, 10))

    # Señal sin ruido (Cuantizada)
    plt.subplot(3, 1, 1)
    plt.plot(t, ycuantizada, color='blue', drawstyle='steps-mid', linewidth=2, label='Señal Cuantizada Pura')
    plt.title(f'Señal Original Sin Ruido (Potencia = {Py:.4f})', fontweight='bold')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.xlim(0, 0.3) # Mantenemos el zoom para ver bien la forma
    plt.legend(loc='upper right')

    # Señal + Ruido 1 (Varianza Baja)
    plt.subplot(3, 1, 2)
    plt.plot(t, ycuantizada, color='blue', drawstyle='steps-mid', alpha=0.3) # Original de fondo
    plt.plot(t, Ysucia1, color='orange', label=f'Señal + Ruido 1 (Pr ≈ {Pr1:.4f})')
    plt.title('Efecto del Ruido 1 (Baja Varianza)', fontweight='bold')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.xlim(0, 0.3)
    plt.legend(loc='upper right')

    # Señal + Ruido 2 (Varianza Alta)
    plt.subplot(3, 1, 3)
    plt.plot(t, ycuantizada, color='blue', drawstyle='steps-mid', alpha=0.3) # Original de fondo
    plt.plot(t, Ysucia2, color='red', label=f'Señal + Ruido 2 (Pr ≈ {Pr2:.4f})')
    plt.title('Efecto del Ruido 2 (Alta Varianza)', fontweight='bold')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.xlim(0, 0.3)
    plt.legend(loc='upper right')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

