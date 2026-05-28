import numpy as np
import matplotlib.pyplot as plt

def zplane(b, a):
    """Función para graficar el diagrama de Polos y Ceros"""
    # Calculamos los ceros y los polos usando np.roots (como pide el enunciado)
    ceros = np.roots(b)
    polos = np.roots(a)
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Dibujamos el círculo unitario
    circulo = plt.Circle((0, 0), 1, color='black', fill=False, linestyle='--')
    ax.add_patch(circulo)
    ax.axhline(0, color='gray', lw=1)
    ax.axvline(0, color='gray', lw=1)
    
    # Graficamos los polos (X) y los ceros (O)
    ax.plot(np.real(ceros), np.imag(ceros), 'o', markersize=9, color='blue', fillstyle='none', label='Ceros')
    ax.plot(np.real(polos), np.imag(polos), 'x', markersize=9, color='red', label='Polos')
    
    # Configuraciones estéticas
    ax.set_title('Plano Z: Diagrama de Polos y Ceros\n(Notar la cancelación en z=1)', fontweight='bold')
    ax.set_xlabel('Parte Real')
    ax.set_ylabel('Parte Imaginaria')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.grid(True, linestyle=':')
    ax.legend(loc='upper right')
    
    return fig, ax

def main():
    # Definición de la Función de Transferencia ---
    b = [1, -2, 2, -1]          # Coeficientes del numerador (z^0, z^-1, z^-2, z^-3)
    
    # Denominador
    # (1 - 1z^-1) * (1 - 0.5z^-1) * (1 - 0.2z^-1)
    a = [1, -1.7, 0.8, -0.1]
    
    # PARTE 1
    zplane(b, a)
    
    # PARTE 2
    N = 30 
    n = np.arange(N)
    
    # Impulso puro en n=0 (delta)
    x = np.zeros(N)
    x[0] = 1.0
    
    y = np.zeros(N)

    for i in range(N):
        # Asignamos valores temporales en cero si el índice es negativo (pasado inexistente)
        x_0 = x[i]
        x_1 = x[i-1] if i-1 >= 0 else 0.0
        x_2 = x[i-2] if i-2 >= 0 else 0.0
        x_3 = x[i-3] if i-3 >= 0 else 0.0
        
        y_1 = y[i-1] if i-1 >= 0 else 0.0
        y_2 = y[i-2] if i-2 >= 0 else 0.0
        y_3 = y[i-3] if i-3 >= 0 else 0.0
        
        y[i] = x_0 - 2*x_1 + 2*x_2 - x_3 + 1.7*y_1 - 0.8*y_2 + 0.1*y_3

    fig, ax = plt.subplots(figsize=(11, 4))
    ax.stem(n, y, linefmt='g-', markerfmt='go', basefmt='k-')
    
    ax.set_title('Respuesta al Impulso $h[n]$ calculada mediante Ecuación de Diferencias', fontweight='bold')
    ax.set_xlabel('Muestras (n)')
    ax.set_ylabel('Amplitud')
    ax.set_xticks(np.arange(0, N, 2))  # Marcas numéricas claras en el eje X
    ax.grid(True, linestyle=':')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()