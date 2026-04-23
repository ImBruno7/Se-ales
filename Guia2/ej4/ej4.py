import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def main():
    N = 20
    n = np.arange(0, N)

    x = np.zeros(N)
    x[0]= 1

    y1 = np.zeros(N)

    y2= np.zeros(N)

    y3 = np.zeros(N)

    for i in n:
        # Funcion 1
        if ((i-2)<0):
            y1[i] = x[i]
        else:
            y1[i] = x[i]+y1[i-2]

        # Funcion 2
        if ((i-1)<0):
            y2[i] = x[i]
        
        else:
            y2[i] = x[i-1]*0.5 + x[i]

        # Funcion 3
        if((i-1)<0):
            if((i-2)<0):
                y3[i] = x[i]
            else: 
                y3[i] = x[i]+ 0.5* y3[i-1]
        else:
            y3[i] = x[i]+ 0.5*y3[i-1] - 0.25* y3[i-2]
   
   
   

    
    fig, axs = plt.subplots(2,2, figsize = (12, 8))
    plt.subplots_adjust(hspace = 0.5, wspace=0.3)


    axs[0,0].stem(n, x)
    axs[0,0].set_title(r' x[n] = delta dirac')
    axs[0,0].grid(True)
    
    axs[0,1].stem(n, y1)
    axs[0,1].set_title(r'1. $y[n] = x[n] + y[n-2]$')
    axs[0,1].grid(True)
    
    axs[1,1].stem(n,y2)
    axs[1,1].set_title(r'2. $y[n] = x[n] + 0.5*x[n-1]$')
    axs[1,1].grid(True)

    axs[1,0].stem(n,y3)
    axs[1,0].set_title(r'3. $y[n] = x[n] + 0.5 * y[n-1] - 0.25* y[n-2]$')
    axs[1,0].grid(True)
    

    plt.show()


main()