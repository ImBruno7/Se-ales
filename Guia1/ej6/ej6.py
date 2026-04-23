import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1

def main():
    fm0=10
    fm1=40
    t, y = f1.generar_senoidal(fs=0.5, fm=fm0, phi=0, t_inicio=0, t_fin=2)

    t_interpolado,y_interpolado = f1.interpolar(t,y,fm0,fm1,f1.sinc_interpoladora)

    plt.figure(figsize=(14, 7))

    # Usamos marcadores grandes para destacar los puntos originales
    markerline_orig, stemlines_orig, baseline_orig = plt.stem(
        t, y, 
        linefmt='grey', markerfmt='D', basefmt='None', 
        label='Original (10 Hz)'
    )
    # Ajustamos el tamaño del rombo original para que se vea bien
    plt.setp(markerline_orig, markersize=10, alpha=0.6)
    # Hacemos las líneas grises más finas
    plt.setp(stemlines_orig, linewidth=1, alpha=0.3)


    # Graficamos la señal INTERPOLADA (puntos azules chicos)
    markerline_interp, stemlines_interp, baseline_interp = plt.stem(
        t_interpolado, y_interpolado, 
        linefmt='C0-', markerfmt='o', basefmt='None', 
        label='Interpolada Sinc (40 Hz)'
    )
    # Ajustamos el tamaño del punto azul para que sea más chico y denso
    plt.setp(markerline_interp, markersize=4)
    # Hacemos las líneas azules finas
    plt.setp(stemlines_interp, linewidth=0.5, alpha=0.5)


    #otros ajustes
    plt.ylim(-1.2, 1.2)
    plt.xlim(t[0]-0.05, t[-1]+0.05) # Un poco de aire en los bordes
    plt.title("Ejercicio 6: Interpolación Sinc (Sobremuestreo 4x) - Comparativa de Puntos")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    
    # Agregamos la leyenda para saber qué es cada cosa
    plt.legend(loc='upper right', fontsize=12)
    
    plt.grid(True, which='both', linestyle='--', alpha=0.5)
    plt.axhline(0, color='black', linewidth=1)

    plt.tight_layout()
    plt.show()


main()

