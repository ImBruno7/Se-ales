import numpy as np
import matplotlib.pyplot as plt

def main():
    n = np.arange(-5, 16) # Vamos desde -5 hasta 15 para ver el antes y el después

    # Pulso rectangular de amplitud 1 entre n=0 y n=5
    x = np.zeros_like(n, dtype=float)
    x[(n >= 0) & (n <= 5)] = 1.0

    # Sistema 1: y[n] = g[n]x[n], donde g[n] = A*sin(w*n*T)
    A = 1.5
    wT = 0.5 * np.pi
    g = A * np.sin(wT * n)
    y1 = g * x

    # Sistema 2: y[n] = sumatoria de x[k] desde k=n-no hasta n+no (Filtro de media móvil)
    no = 2
    y2 = np.zeros_like(n, dtype=float)
    # Recorremos cada instante 'n'
    
    for i, n_instante in enumerate(n):
        ventana = (n >= n_instante - no) & (n <= n_instante + no)
        y2[i] = np.sum(x[ventana])

    # Sistema 3: y[n] = x[n] + 2
    y3 = x + 2

    # Sistema 4: y[n] = n * x[n]
    y4 = n * x

    #grafica
    plt.figure(figsize=(12, 14))

    # Entrada original
    plt.subplot(5, 1, 1)
    plt.stem(n, x, basefmt="black", linefmt="blue", markerfmt="bo")
    plt.title('Señal de Entrada: x[n] (Pulso Rectangular)', fontweight='bold')
    plt.grid(True)
    plt.ylabel('Amplitud')

    # Salida Sist 1
    plt.subplot(5, 1, 2)
    plt.stem(n, y1, basefmt="black", linefmt="orange", markerfmt="o")
    plt.title('Sistema 1: y[n] = g[n]x[n]', fontweight='bold')
    plt.grid(True)
    plt.ylabel('Amplitud')

    # Salida Sist 2
    plt.subplot(5, 1, 3)
    plt.stem(n, y2, basefmt="black", linefmt="green", markerfmt="go")
    plt.title(f'Sistema 2: Sumatoria móvil con no={no}', fontweight='bold')
    plt.grid(True)
    plt.ylabel('Amplitud')

    # Salida Sist 3
    plt.subplot(5, 1, 4)
    plt.stem(n, y3, basefmt="black", linefmt="red", markerfmt="ro")
    plt.title('Sistema 3: y[n] = x[n] + 2 ', fontweight='bold')
    plt.grid(True)
    plt.ylabel('Amplitud')

    # Salida Sist 4
    plt.subplot(5, 1, 5)
    plt.stem(n, y4, basefmt="black", linefmt="purple", markerfmt="mo")
    plt.title('Sistema 4: y[n] = n * x[n]', fontweight='bold')
    plt.xlabel('Muestras (n)')
    plt.ylabel('Amplitud')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

main()