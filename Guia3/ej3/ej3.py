import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3

def main():
    t = np.linspace(-1,1,1000)
    y = np.where(t<0,-1,1)

    #parte 1
    y_aprox = 45/16 * t - 35/16 * (t**3)

    ECT = (fG3.Norma(y-y_aprox,2))**2
    print("\n" + "="*40)
    print("      Error Cuadratico Total (ECT)")
    print(f"{ECT:.3f}")
    
    #parte 2
    coef1,coef2 = f1.generar_ruido(n=100,media=45/16,varianza=1),f1.generar_ruido(n=100,media=-35/16,varianza=1)
    v2ECT = np.zeros(len(coef2))
    for i in range(len(coef2)):
        y2_aprox =  coef1[i] * t - coef2[i] * (t**3)
        v2ECT[i] = (fG3.Norma(y-y2_aprox,2))**2
        #print("\n" + "="*40)
        #print(f"      Vector de Error Cuadratico Total (vECT) en la iteracion")
        #print(f"{v2ECT[i]:.3f}")

    # Crear la figura 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Graficar los puntos sueltos de tus iteraciones
    ax.scatter(coef1, coef2, v2ECT, color='blue')

    # Etiquetas de los ejes
    ax.set_title('Error vs Variación Aleatoria de Coeficientes')
    ax.set_xlabel('Coeficiente 1')
    ax.set_ylabel('Coeficiente 3')
    ax.set_zlabel('Vector ECT')

    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    
    main()

