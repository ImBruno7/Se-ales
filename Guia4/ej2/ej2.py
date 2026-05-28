import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3

def main():
    t,s1 = f1.generar_senoidal(A = 1, fs = 2, fm = 100, phi = 0, t_inicio = 0, t_fin = 1)
    _,s2 = f1.generar_onda_cuadrada(fs = 2, fm = 100, phi = 0, t_inicio = 0, t_fin = 1)
    _,s3 = f1.generar_senoidal(A = 1, fs = 4, fm = 100, phi = 0, t_inicio = 0, t_fin = 1)

    #parte 1
    Ps1s2 = np.dot(s1,s2)
    Ps1s3 = np.dot(s1,s3)
    Ps2s3 = np.dot(s2,s3)

    print("\n" + "="*40)
    print("Parte 1")
    print(f"Prod Interno S1 y S2: {Ps1s2:.3f}")
    print(f"Prod Interno S1 y S3: {Ps1s3:.3f}")
    print(f"Prod Interno S2 y S3: {Ps2s3:.3f}")

    #parte 2
    print("\n" + "="*40)
    print("Parte 2")
    tf1 = np.fft.fft(s1)
    tf2 = np.fft.fft(s2)
    tf3 = np.fft.fft(s3)

    Ptf1tf2 = np.vdot(tf1,tf2)
    Ptf1tf3 = np.vdot(tf1,tf3)
    Ptf2tf3 = np.vdot(tf2,tf3)
    print(f"Prod Interno TF1 y TF2: {Ptf1tf2:.3f}")
    print(f"Prod Interno TF1 y TF3: {Ptf1tf3:.3f}")
    print(f"Prod Interno TF2 y TF3: {Ptf2tf3:.3f}")

    #parte 3
    print("\n" + "="*40)
    print("Parte 3")
    _,s3 = f1.generar_senoidal(A = 1, fs = 3.6, fm = 100, phi = 0, t_inicio = 0, t_fin = 1)

    Ps1s3 = np.vdot(s1,s3)
    print(f"Prod Interno S1 y S3: {Ps1s3:.13f}")

    tf3 = np.fft.fft(s3)
    Ptf1tf3 = np.vdot(tf1,tf3)
    print(f"Prod Interno TF1 y TF3: {Ptf1tf3:.12f}")

if __name__ == "__main__":
    main()
