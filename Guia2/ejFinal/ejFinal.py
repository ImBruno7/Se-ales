import numpy as np
import matplotlib.pyplot as plt
import Guia2.funcConvolucion as fc

def grafica1(n,N,x,h):
    # gráfica facha
    plt.figure(figsize=(10, 5))
    
    # Graficamos con 'stem' (ideal para señales discretas)
    plt.stem(n, h, basefmt="black", linefmt="dodgerblue", markerfmt="bo")
    
    # Títulos y etiquetas
    plt.title('Respuesta al Impulso $h[n]$ (Sistema IIR)', fontweight='bold', fontsize=14)
    plt.xlabel('Muestras (n)', fontsize=12)
    plt.ylabel('Amplitud', fontsize=12)
    
    # Estética: límites y grilla
    plt.xlim(-1, 20)
    plt.ylim(0, 1.2)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Agregamos la caja de texto con la conclusión de estabilidad para el informe
    texto_conclusion = (
        "Análisis de Estabilidad:\n"
        "Como la amplitud decae asintóticamente\n"
        "hacia cero con el paso del tiempo,\n"
        "se comprueba que el sistema es ESTABLE."
    )
    plt.text(7, 0.7, texto_conclusion, 
             bbox=dict(facecolor='lightgreen', alpha=0.3, edgecolor='green', boxstyle='round,pad=0.8'),
             fontsize=11)

    plt.tight_layout()
    plt.show()

def MatrizConv(h,L,M,N):
    Matriz = np.zeros((L,M))
    for i in range(M):
        aux = np.concatenate([np.zeros(i),h,np.zeros(L-i-N)])
        Matriz[:,i]= aux
    return Matriz
    
def main():
    N = 20
    x = np.zeros(N)
    x[0] = 1
    h = np.zeros(N)
    for i in range(N):
        h[i] = x[i] if i == 0 else x[i] + 0.2 * x[i-1] + 0.6 * h[i-1]
    
    n = np.arange(N)
    
    grafica1(n,N,x,h)

    #parte 2
    M = 10
    L = N + M -1
    xAux = np.arange(1,M+1)
   

    y1 = fc.convolucion(xAux,h)

    Matriz = MatrizConv(h,L,M,N)
    y2 = np.dot(Matriz,xAux)
    
    printMatriz(Matriz,xAux,y2)

    x3 = np.concatenate([xAux,np.zeros(L-M)])
    h3 = np.concatenate([h,np.zeros(L-N)])

    y3 = fc.convCircular(x3,h3)

    grafica2(y1,y2,y3,L)
    

def grafica2(y1,y2,y3,L):
    # Gráficas Aesthetic para el TP
    n_y = np.arange(L) # Eje de tiempo de 0 a 28

    fig, axs = plt.subplots(3, 1, figsize=(10, 10))
    fig.suptitle('Parte III: Comparación de Métodos de Convolución', fontsize=16, fontweight='bold')

    # Convolución Lineal
    axs[0].stem(n_y, y1, basefmt="black", linefmt="dodgerblue", markerfmt="bo", label="y1[n]")
    axs[0].set_title('Método A: Sumatoria de Convolución (Lineal)', fontweight='bold')
    axs[0].grid(True, linestyle='--', alpha=0.6)
    axs[0].legend(loc="upper right")
    axs[0].set_xlim(-1, 30)
    axs[0].set_ylim(-2, np.max(y1) + 5)

    # Convolución Matricial
    axs[1].stem(n_y, y2, basefmt="black", linefmt="orange", markerfmt="o", label="y2[n]")
    axs[1].set_title('Método B: Multiplicación Matricial (H · x)', fontweight='bold')
    axs[1].grid(True, linestyle='--', alpha=0.6)
    axs[1].legend(loc="upper right")
    axs[1].set_xlim(-1, 30)
    axs[1].set_ylim(-2, np.max(y2) + 5)

    # Convolución Circular
    axs[2].stem(n_y, y3, basefmt="black", linefmt="limegreen", markerfmt="go", label="y3[n]")
    axs[2].set_title('Método C: Convolución Circular Equivalente (con Zero-Padding)', fontweight='bold')
    axs[2].set_xlabel('Muestras (n)', fontsize=12)
    axs[2].grid(True, linestyle='--', alpha=0.6)
    axs[2].legend(loc="upper right")
    axs[2].set_xlim(-1, 30)
    axs[2].set_ylim(-2, np.max(y3) + 5)

    plt.tight_layout()
    plt.subplots_adjust(top=0.92) # Espacio para que el título principal no se pise
    plt.show()

def printMatriz(Matriz,xAux,y2):
    # Prints del Método Matricial
    print("\n" + "="*50)
    print("      MÉTODO B: ÁLGEBRA LINEAL (Y = H · x)")
    print("="*50)
    
    print(f"\n1. Vector de Entrada x (Dimensiones: {xAux.shape}):")
    print(xAux)
    
    print(f"\n2. Matriz de Convolución H (Dimensiones: {Matriz.shape}):")
    # np.round ayuda a que los números con muchos decimales no deformen la matriz al imprimirla
    print(np.round(Matriz, 3)) 
    
    print(f"\n3. Resultado Y (Dimensiones: {y2.shape}):")
    print(np.round(y2, 3))
    print("="*50 + "\n")

if __name__ == "__main__":
    main()