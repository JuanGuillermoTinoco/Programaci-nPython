#Ejercicio 1 a). Fecha: 02/Dic/16. Laboratorio 3B.
#Juan Guillermo Urincho Tinoco.

import math as m
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-6,2)
y=(x**2)-(4*x)+5
plt.plot(x,y,linewidth=3,color='r',label='Linea 1')
plt.legend()
plt.title("Grafica a")
plt.xlabel('Tiempo libre')
plt.ylabel('Escuela')
plt.grid(True)
plt.show()
