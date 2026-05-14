import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3

def main():
    t = np.linspace(-1,1,1000)
    y = np.where(t<0,-1,1)

    #parte 1
    c1_opt = 3/2
    c3_opt = -7/8
    P1 = t
    P3 = 0.5 * (5 * t**3 - 3 * t)
    y_aprox =  c1_opt * P1 + c3_opt * P3

    ECT = (fG3.Norma(y-y_aprox,2))**2
    print("\n" + "="*40)
    print("      Error Cuadratico Total (ECT)")
    print(f"{ECT:.3f}")
    
    #parte 2
    coef1,coef2 = f1.generar_ruido(n=200,media=c1_opt,varianza=1),f1.generar_ruido(n=200,media=c3_opt,varianza=1)
    v2ECT = np.zeros(len(coef2))
    for i in range(len(coef2)):
        y2_aprox =  coef1[i] * P1 + coef2[i] * P3
        v2ECT[i] = (fG3.Norma(y-y2_aprox,2))**2
        #print("\n" + "="*40)
        #print(f"      Vector de Error Cuadratico Total (vECT) en la iteracion")
        #print(f"{v2ECT[i]:.3f}")

    # Crear la figura 3D
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Graficamos con trisurf
    ax.plot_trisurf(coef1, coef2, v2ECT, cmap='viridis', alpha=0.7, edgecolor='none')
    
    # Marcamos el punto óptimo
    ax.scatter(c1_opt, c3_opt, ECT, color='red', s=100, label='Mínimo (Óptimo)', zorder=5)

    ax.set_title('(Bases Ortogonales)')
    ax.set_xlabel('Coeficiente Alfa 1 (Legendre)')
    ax.set_ylabel('Coeficiente Alfa 3 (Legendre)')
    ax.set_zlabel('Error Cuadrático Total (ECT)')
    
    import matplotlib.lines as mlines
    punto_rojo = mlines.Line2D([], [], color='red', marker='o', linestyle='None',
                               markersize=10, label='Mínimo (Óptimo)')
    ax.legend(handles=[punto_rojo])

    plt.show()

    #parte 3
    max_coef = 10
    vECT_historial = np.zeros(max_coef)
    y_aprox = 0

    for n in range(max_coef):
        alfa_n, phi_n = fG3.calcular_termino_legendre(n, t, y)
        
        y_aprox += alfa_n * phi_n
        
        # Calculamos el ECT de esta iteración
        vECT_historial[n] = (fG3.Norma(y-y_aprox,2))**2

    print(f"Aproximacion con 2 (en realidad 4) coeficientes: {vECT_historial[3]}")

    # Graficar la curva
    plt.figure()
    plt.plot(range(1, max_coef + 1), vECT_historial, marker='o', color='red')
    plt.title('Evolución del ECT al sumar coeficientes de Legendre')
    plt.xlabel('Cantidad de coeficientes utilizados')
    plt.ylabel('Error Cuadrático Total')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    
    main()

