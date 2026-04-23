import numpy as np
import matplotlib.pyplot as plt
import Guia1.ej1.funciones as f1
import Guia1.ej2.funcionesej2 as f2
import Guia3.funcionesG3 as fG3

def main():
    _,ySin = f1.generar_senoidal(fs=30, fm =97, phi=0, t_inicio=0, t_fin=1)
    t,yCuad = f1.generar_onda_cuadrada(fs=30, fm =97, phi=0, t_inicio=0, t_fin=1)
    n = len(ySin)
    yRampa = np.arange(1,n)
    yAleatoria = f1.generar_ruido(n = n ,media = 0,varianza = 5)

    #Valor Medio
    print("="*40 + "\n")
    print("="*40 + "\n")
    print("="*40 + "\n")
    print("="*40 + "\n")
    print("      Inicio")
    print("\n" + "="*40)
    print("      VALOR MEDIO")
    print(f"1. Señal Senoidal:  {np.sum(ySin)/n:.3f}")
    print(f"2. Señal Cuadrada:  {np.sum(yCuad)/n:.3f}")
    print(f"3. Señal Rampa:     {np.sum(yRampa)/n:.3f}")
    print(f"4. Señal Aleatoria: {np.sum(yAleatoria)/n:.3f}")
    #Max
    print("\n" + "="*40)
    print("      Valor Maximo")
    print(f"1. Señal Senoidal:  {max(ySin):.3f}")
    print(f"2. Señal Cuadrada:  {max(yCuad):.3f}")
    print(f"3. Señal Rampa:     {max(yRampa):.3f}")
    print(f"4. Señal Aleatoria: {max(yAleatoria):.3f}")
    #Min
    print("\n" + "="*40)
    print("      Valor Minimo")
    print(f"1. Señal Senoidal:  {min(ySin):.3f}")
    print(f"2. Señal Cuadrada:  {min(yCuad):.3f}")
    print(f"3. Señal Rampa:     {min(yRampa):.3f}")
    print(f"4. Señal Aleatoria: {min(yAleatoria):.3f}")
    #Amplitud
    print("="*40 + "\n")
    print("      Amplitud")
    print(f"1. Señal Senoidal:  {fG3.Norma(ySin,"inf"):.3f}")
    print(f"2. Señal Cuadrada:  {fG3.Norma(yCuad,"inf"):.3f}")
    print(f"3. Señal Rampa:     {fG3.Norma(yRampa,"inf"):.3f}")
    print(f"4. Señal Aleatoria: {fG3.Norma(yAleatoria,"inf"):.3f}")
    #Energia
    print("="*40 + "\n")
    print("      Energia")
    print(f"1. Señal Senoidal:  {(fG3.Norma(ySin,2)**2):.3f}")
    print(f"2. Señal Cuadrada:  {(fG3.Norma(yCuad,2)**2):.3f}")
    print(f"3. Señal Rampa:     {(fG3.Norma(yRampa,2)**2):.3f}")
    print(f"4. Señal Aleatoria: {(fG3.Norma(yAleatoria,2)**2):.3f}")
    #Accion
    print("="*40 + "\n")
    print("      Accion")
    print(f"1. Señal Senoidal:  {fG3.Norma(ySin,1):.3f}")
    print(f"2. Señal Cuadrada:  {fG3.Norma(yCuad,1):.3f}")
    print(f"3. Señal Rampa:     {fG3.Norma(yRampa,1):.3f}")
    print(f"4. Señal Aleatoria: {fG3.Norma(yAleatoria,1):.3f}")
    #Potencia Media
    print("="*40 + "\n")
    print("      Potencia Media")
    print(f"1. Señal Senoidal:  {(fG3.Norma(ySin,2)**2)/(2*n):.3f}")
    print(f"2. Señal Cuadrada:  {(fG3.Norma(yCuad,2)**2)/(2*n):.3f}")
    print(f"3. Señal Rampa:     {(fG3.Norma(yRampa,2)**2)/(2*n):.3f}")
    print(f"4. Señal Aleatoria: {(fG3.Norma(yAleatoria,2)**2)/(2*n):.3f}")
    #RMS
    print("="*40 + "\n")
    print("      RMS")
    print(f"1. Señal Senoidal:  {np.sqrt((fG3.Norma(ySin,2)**2)/(2*n)):.3f}")
    print(f"2. Señal Cuadrada:  {np.sqrt((fG3.Norma(yCuad,2)**2)/(2*n)):.3f}")
    print(f"3. Señal Rampa:     {np.sqrt((fG3.Norma(yRampa,2)**2)/(2*n)):.3f}")
    print(f"4. Señal Aleatoria: {np.sqrt((fG3.Norma(yAleatoria,2)**2)/(2*n)):.3f}")


if __name__ == "__main__":
    
    main()


