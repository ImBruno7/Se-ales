import numpy as np
import matplotlib.pyplot as plt
import Guia2.funcConvolucion as fc

    
def main():
    N = 40
    a = 0.8
    #armamos el delta y el x
    delta = np.zeros(N)
    delta[0] = 1
    x = np.zeros(N)
    for i in range(N):
        x[i] = delta[i] if i == 0 else delta[i] - a* delta[i-1]
    
    #armamos los vectores de hA y hB
    n = np.arange(N)

    hA = np.sin(8*n)
    hB = a**n

    # ORDEN 1: x -> hA -> hB
    w1 = fc.convolucion(x, hA)
    y1 = fc.convolucion(w1, hB)

    # ORDEN 2: x -> hB -> hA
    w2 = fc.convolucion(x, hB)
    y2 = fc.convolucion(w2, hA)
    
    # --- Gráficos ---
    fig, axs = plt.subplots(3, 2, figsize=(15, 12))
    plt.subplots_adjust(hspace=0.5)

    # Fila 1: respuestas al impulso
    axs[0, 0].stem(n, hA, linefmt='C0-', markerfmt='C0o')
    axs[0, 0].set_title(r'Sistema A: $h_A[n] = \sin(8n)$')

    axs[0, 1].stem(n, hB, linefmt='C1-', markerfmt='C1o')
    axs[0, 1].set_title(r'Sistema B: $h_B[n] = 0.8^n$')

    # Los w
    axs[1, 0].stem(range(len(w1)), w1, linefmt='C2-', markerfmt='C2o')
    axs[1, 0].set_title(r'Intermedio 1: $w_1 = x[n] * h_A[n]$')
    axs[1, 0].set_xlim(0, N)

    axs[1, 1].stem(range(len(w2)), w2, linefmt='C4-', markerfmt='C4o')
    axs[1, 1].set_title(r'Intermedio 2: $w_2 = x[n] * h_B[n]$ (¡Es un Delta!)')
    axs[1, 1].set_xlim(0, N)

    # Resultados
    axs[2, 0].stem(range(len(y1)), y1, linefmt='C0-', markerfmt='C0o')
    axs[2, 0].set_title('Salida Final: Orden A -> B')
    axs[2, 0].set_xlim(0, N)

    axs[2, 1].stem(range(len(y2)), y2, linefmt='C3--', markerfmt='C3x')
    axs[2, 1].set_title('Salida Final: Orden B -> A')
    axs[2, 1].set_xlim(0, N)

    for ax in axs.flat:
        ax.grid(True, alpha=0.3)

    plt.show()

    plt.tight_layout()
    plt.show()

    # Verificación de conmutatividad
    print(f"¿Son idénticas las salidas?: {np.allclose(y1, y2)}")

    

if __name__ == "__main__":
    main()