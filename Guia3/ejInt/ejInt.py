import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3


def main():

    t ,aux1 = f1.generar_senoidal(fs = 100, fm = 1000, phi = 0, t_inicio = 0, t_fin =0.5)
    aux2 = f1.generar_ruido(n=len(aux1),media = 0, varianza = 0.5)
    signal = aux1 + aux2
   
    Norma_2 = fG3.Norma(x=signal, p=2)
    Energia = Norma_2 ** 2
    RMS = np.sqrt(Energia / (2 * len(signal)))

    Accion = fG3.Norma(x=signal, p=1) 
    Amplitud = fG3.Norma(x=signal, p="inf") 

    # prints de resultados
    print("-" * 30)
    print("Metricas Parte 1")
    print("-" * 30)
    print(f"Norma-2:   {Norma_2:.2f}")
    print(f"Energía:   {Energia:.2f}")
    print(f"Valor RMS: {RMS:.2f}")
    print(f"Acción:    {Accion:.2f}")
    print(f"Amplitud:  {Amplitud:.2f}")
    print("-" * 30)

    # Gráfica
    plt.figure(figsize=(10, 4))
    # Graficamos la señal con ruido
    plt.plot(t, signal, label='x[n] (100Hz + Ruido)', color='dodgerblue')
    # Agregamos la señal pura de fondo para que quede bien visual el efecto del ruido
    plt.plot(t, aux1, label='Senoidal pura (Referencia)', color='darkorange', linestyle='--', alpha=0.8)

    plt.title('Parte I: Señal Compuesta vs Señal Original')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend(loc='upper right')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.show()

    #parte 2
    y = aux1 #signal de 100hz
    ProdInt = np.dot(signal,y)
    norma_y = fG3.Norma(y,2)
    tita = np.arccos(ProdInt/(norma_y * Norma_2))
    print("Metricas Parte 2")
    print("-" * 30)
    print(f"Producto Interno:  {ProdInt:.2f}")
    print(f"Angulo entre las señales: {(tita*180)/np.pi:.2f}")

    #parte 3
    # Generamos la segunda senoidal de 200 Hz
    _, aux_200 = f1.generar_senoidal(fs=200, fm=1000, phi=0, t_inicio=0, t_fin=0.5)

    # Volvemos ortonormales a los vectores base
    phi1 = aux1 / fG3.Norma(aux1, 2)
    phi2 = aux_200 / fG3.Norma(aux_200, 2)

    # Calculamos los coeficientes de proyección
    alpha1 = np.dot(signal, phi1)
    alpha2 = np.dot(signal, phi2)

    # Construimos la señal aproximada
    y_aprox = alpha1 * phi1 + alpha2 * phi2

    # Calculamos el Error Cuadrático Total (Norma-2 del vector de error al cuadrado)
    vector_error = signal - y_aprox
    error_cuadratico_total = fG3.Norma(vector_error, 2) ** 2

    print(f"Coeficiente alpha 1 (100 Hz): {alpha1:.2f}")
    print(f"Coeficiente alpha 2 (200 Hz): {alpha2:.2f}")
    print(f"Error Cuadrático Total:       {error_cuadratico_total:.2f}")

    # Gráfica Parte 3
    print("Metricas Parte 2")
    plt.figure(figsize=(10, 4))
    # Dibujamos la señal original ruidosa de fondo
    plt.plot(t, signal, label='y[n] Original (Ruidosa)', color='lightgray')
    # Dibujamos la aproximación arriba
    plt.plot(t, y_aprox, label='~y[n] Aproximada (Proyección)', color='red', linewidth=2)
    
    plt.title('Parte III: Señal Original vs Aproximación')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.legend(loc='upper right')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.tight_layout()
    plt.show()

    #Parte 4
    print("Métricas Parte 4")
    print("-" * 30)
    
    _, y_90 = f1.generar_senoidal(fs=100, fm=1000, phi=np.pi/2, t_inicio=0, t_fin=0.5)
    ProdInt_90 = np.dot(signal, y_90)
    
    print(f"Producto Interno con fase 90°: {ProdInt_90:.2f}")

    "El valor residual que se obtenga corresponderá únicamente a la coincidencia aleatoria con el ruido."

if __name__ == "__main__":
    main()