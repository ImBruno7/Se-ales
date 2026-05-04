import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3

def detectar_tecla(pedacito):
    """
    Recibe un recorte de audio, busca sus frecuencias y devuelve el caracter de la tecla.
    """
    freqs_filas = [697, 770, 852, 941]
    freqs_columnas = [1209, 1336, 1477]
    
    teclado = {
        (697, 1209): '1', (697, 1336): '2', (697, 1477): '3',
        (770, 1209): '4', (770, 1336): '5', (770, 1477): '6',
        (852, 1209): '7', (852, 1336): '8', (852, 1477): '9',
        (941, 1209): '*', (941, 1336): '0', (941, 1477): '#'
    }
    
    # Buscamos los ganadores usando nuestra función auxiliar
    fila = fG3.obtener_mejor_frecuencia(pedacito, freqs_filas)
    columna = fG3.obtener_mejor_frecuencia(pedacito, freqs_columnas)
    
    # Cruzamos los datos en el diccionario y devolvemos el string
    return teclado[(fila, columna)]

def main():

     # Carga todos los datos del archivo en un vector
    senal_ruidosa = np.loadtxt('Guia3/te.txt')
    # Podemos ver cuántas muestras tiene en total
    muestras_totales = len(senal_ruidosa)
    print(f"El archivo tiene {muestras_totales} muestras.")

    # Graficamos la señal cruda para ver dónde están los números
    plt.figure(figsize=(12, 4))
    plt.plot(senal_ruidosa, color='navy')
    plt.title('Señal de audio completa (te.txt)')
    plt.xlabel('Muestras')
    plt.ylabel('Amplitud')
    plt.grid(True)
    plt.show()

    umbral = 1.2
    muestras_por_numero = 4000
    
    numeros_recortados = [] # Acá vamos a guardar los 7 pedacitos
    i = 0
    
    while i < len(senal_ruidosa):
        # Si la amplitud en valor absoluto supera el umbral entonces hay algo mas que ruido
        if abs(senal_ruidosa[i]) > umbral:
            
            # Recortamos desde este punto, 4000 muestras hacia adelante
            pedacito = senal_ruidosa[i : i + muestras_por_numero]
            numeros_recortados.append(pedacito)
            
            # Pegamos un salto largo para esquivar el resto de este sonido 
            i += 6500 
        else:
            # Si es solo ruido de fondo, avanzamos de a 1 muestra
            i += 1
            
    print(f"Se encontraron {len(numeros_recortados)} números.")
    
    numero_descubierto = ""
    
    for pedacito in numeros_recortados:
        tecla = detectar_tecla(pedacito)
        numero_descubierto += tecla
        
    print(f"Num de telfeono: {numero_descubierto}")
    

    



if __name__ == "__main__":
    
    main()


    
