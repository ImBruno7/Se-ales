import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3

def main():
    _, s1 = f1.generar_senoidal(fs=15, fm=100, phi=0, t_inicio=0, t_fin=2)
    _, s2 = f1.generar_senoidal(fs=15, fm=100, phi=np.pi, t_inicio=0, t_fin=2)
    A1,A2 = 10,2
    s1 = A1 * s1
    s2 = A2 * s2
    print("\n" + "="*40)
    print("      Producto Interno")
    print(f"{np.dot(s1,s2):.3f}")

if __name__ == "__main__":
    
    main()


