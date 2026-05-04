import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3


def main():
    bases = []
    fm = 60
    s = np.zeros(fm+1)

    for i in range(10):
        t, s_aux = f1.generar_senoidal(fs = i+1, fm = fm, phi = 0, t_inicio = 0, t_fin =1)
        bases.append(s_aux)
        s += np.random.uniform(0, 5) * s_aux
    
    # --- PARTE 1: MEDIR EL GRADO DE PARECIDO ---
    dt = t[1] - t[0]
    parecidos = np.zeros(10)
    
    for i in range(10):
        parecidos[i] = np.sum(s * bases[i]) * dt #integral del producto interno
        
    # --- GRÁFICO DE BARRAS ---
    frecuencias = np.arange(1, 11) # Eje X: frecuencias del 1 al 10
    
    plt.figure(figsize=(8, 5))
    plt.bar(frecuencias, parecidos, color='skyblue', edgecolor='black')
    
    plt.title('Grado de parecido entre la señal mezcla y las bases senoidales')
    plt.xlabel('Frecuencia de la base (Hz)')
    plt.ylabel('Similitud (Producto Interno)')
    plt.xticks(frecuencias) # Para que muestre todos los números del 1 al 10 en el eje X
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()


    # PARTE 2
    s2 = np.zeros(fm+1)

    for i in range(10):
        fase = np.random.uniform(0,1)
        t, s_aux = f1.generar_senoidal(fs = i+1, fm = fm, phi = fase*np.pi, t_inicio = 0, t_fin =1)
        s2 += np.random.uniform(0, 5) * s_aux

    for i in range(10):
        parecidos[i] = np.sum(s2 * bases[i]) * dt #integral del producto interno
        
    # --- GRÁFICO DE BARRAS ---
    frecuencias = np.arange(1, 11) # Eje X: frecuencias del 1 al 10
    
    plt.figure(figsize=(8, 5))
    plt.bar(frecuencias, parecidos, color='skyblue', edgecolor='black')
    
    plt.title('Grado de parecido entre la señal mezcla y las bases senoidales')
    plt.xlabel('Frecuencia de la base (Hz)')
    plt.ylabel('Similitud (Producto Interno)')
    plt.xticks(frecuencias) # Para que muestre todos los números del 1 al 10 en el eje X
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

    #parte 3
    _, s_cuadrada = f1.generar_onda_cuadrada(fs = 5.5, fm=60, phi=0, t_inicio=0, t_fin=1)

    for i in range(10):
        parecidos[i] = np.sum(s_cuadrada * bases[i]) * dt #integral del producto interno
        
    # --- GRÁFICO DE BARRAS ---
    frecuencias = np.arange(1, 11) # Eje X: frecuencias del 1 al 10
    
    plt.figure(figsize=(8, 5))
    plt.bar(frecuencias, parecidos, color='skyblue', edgecolor='black')
    
    plt.title('Grado de parecido entre la señal mezcla y las bases senoidales')
    plt.xlabel('Frecuencia de la base (Hz)')
    plt.ylabel('Similitud (Producto Interno)')
    plt.xticks(frecuencias) # Para que muestre todos los números del 1 al 10 en el eje X
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.show()

if __name__ == "__main__":
    
    main()

