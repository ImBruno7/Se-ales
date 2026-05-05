import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3
from scipy.io import wavfile

def main():
    #Cargamos el audio. scipy nos da el fm exacto que tenga el .wav
    fm, senal = wavfile.read('Guia3/escala.wav')
    
    # Normalizamos la amplitud (opcional pero siempre es buena práctica)
    senal = senal / np.max(np.abs(senal))
    
    # Definimos las frecuencias
    freqs_tabla = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
    
    # La familia de LA en distintas octavas
    familia_la = [110.0, 220.0, 440.0, 880.0, 1760.0]
    
    # Unimos todo en una sola lista (usamos set para borrar los que se repitan, como el 440)
    todas_las_freqs = list(set(freqs_tabla + familia_la))
    
    # Calculamos la ventana de tiempo (0.5 segundos exactos)
    muestras_por_nota = int(fm * 0.5)
    
    # Hachamos la señal en 8 pedacitos de 0.5s y analizamos
    for i in range(8):
        inicio = i * muestras_por_nota
        fin = inicio + muestras_por_nota
        pedacito = senal[inicio:fin]
        
        freq_ganadora = fG3.obtener_mejor_frecuencia(pedacito, todas_las_freqs)
        
        # Verificamos si la frecuencia que sacó más puntaje es LA
        if freq_ganadora in familia_la:
            tiempo_arranque = i * 0.5
            print("-" * 40)
            print(f"LA detectado a {freq_ganadora} Hz")
            print(f"Es la nota número {i + 1} de la secuencia.")
            print(f"Comienza en el segundo {tiempo_arranque}")
            print("-" * 40)




if __name__ == "__main__":
    
    main()
