import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1

def main():
    num_realizaciones = 100
    num_muestras = 1000
    media = 0
    varianza = 1
    # Generamos la matriz completa
    # Varianza unitaria significa desvío = 1
    matriz = np.zeros((num_realizaciones, num_muestras))
    
    for i in range(num_realizaciones):
        for j in range(num_muestras):
            
            matriz[i, j] = f1.generar_un_valor_gaussiano(media, varianza)
    
    
    # Preparamos la figura con 4 gráficos (2 filas, 2 columnas)
    fig, axs = plt.subplots(2, 2, figsize=(16, 12))
    tiempo_n = np.arange(num_muestras)

    # ESTACIONARIEDAD (Promedio en el Ensamble / "Vertical")
    
    media_ensamble = np.mean(matriz, axis=0)
    varianza_ensamble = np.var(matriz, axis=0)

    # Gráfico Estacionariedad - Media 
    axs[0, 0].plot(tiempo_n, media_ensamble, color='blue', alpha=0.7, label='Media del ensamble')
    axs[0, 0].axhline(media, color='red', linestyle='--', linewidth=2, label='Media Teórica (0)')
    axs[0, 0].set_title('Estacionariedad: Media S(Oscila alrededor de 0)')
    axs[0, 0].set_xlabel('Tiempo (n)')
    axs[0, 0].set_ylabel('Valor de Media')
    axs[0, 0].set_ylim(-1.0, 1.0) 
    axs[0, 0].grid(True, alpha=0.3)
    axs[0, 0].legend()

    # Gráfico Estacionariedad - Varianza
    axs[0, 1].plot(tiempo_n, varianza_ensamble, color='orange', alpha=0.7, label='Varianza del ensamble')
    axs[0, 1].axhline(varianza, color='red', linestyle='--', linewidth=2, label='Varianza Teórica (1)')
    axs[0, 1].set_title('Estacionariedad: Varianza (Oscila alrededor de 1)')
    axs[0, 1].set_xlabel('Tiempo (n)')
    axs[0, 1].set_ylabel('Valor de Varianza')
    axs[0, 1].set_ylim(0.0, 2.0) 
    axs[0, 1].grid(True, alpha=0.3)
    axs[0, 1].legend()

    # ERGODICIDAD (Promedio Temporal / "Horizontal" en UNA realización)
    una_realizacion = matriz[0, :]

    media_temporal_acumulada = np.cumsum(una_realizacion) / (tiempo_n + 1)
    varianza_temporal_acumulada = [np.var(una_realizacion[:k+1]) for k in range(num_muestras)]

    # Gráfico Ergodicidad - Media
    axs[1, 0].plot(tiempo_n, media_temporal_acumulada, color='green', linewidth=2, label='Media temporal')
    axs[1, 0].axhline(media, color='red', linestyle='--', linewidth=2, label='Teórica (0)')
    axs[1, 0].set_title('Ergodicidad: Media convergiendo (Se estabiliza en 0)')
    axs[1, 0].set_xlabel('Tiempo (n)')
    axs[1, 0].set_ylabel('Media acumulada')
    axs[1, 0].set_ylim(-1.0, 1.0) 
    axs[1, 0].grid(True, alpha=0.3)
    axs[1, 0].legend()

    # Gráfico Ergodicidad - Varianza
    axs[1, 1].plot(tiempo_n, varianza_temporal_acumulada, color='purple', linewidth=2, label='Varianza temporal')
    axs[1, 1].axhline(varianza, color='red', linestyle='--', linewidth=2, label='Teórica (1)')
    axs[1, 1].set_title('Ergodicidad: Varianza convergiendo (Se estabiliza en 1)')
    axs[1, 1].set_xlabel('Tiempo (n)')
    axs[1, 1].set_ylabel('Varianza acumulada')
    axs[1, 1].set_ylim(0.0, 2.0)
    axs[1, 1].grid(True, alpha=0.3)
    axs[1, 1].legend()

    plt.tight_layout()
    plt.show()



main()
