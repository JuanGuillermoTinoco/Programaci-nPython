#Ejercicio 1 c). Fecha: 02/Dic/16. Laboratorio 3B.
#Juan Guillermo Urincho Tinoco.

import math as m
import matplotlib.pyplot as plt
import numpy as np
t=np.linspace(-1,5)
y=t*m.e**-2*t
plt.plot(t,y,linewidth=3,color='y',label='Linea 3')
plt.legend()
plt.title("Grafica C")
plt.xlabel('Series de Netflix')
plt.ylabel('Consumo de tiempo')
plt.grid(True)
plt.show()
