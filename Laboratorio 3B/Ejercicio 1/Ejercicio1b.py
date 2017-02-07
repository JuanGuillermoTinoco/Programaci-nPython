#Ejercicio 1 b). Fecha: 02/Dic/16. Laboratorio 3B.
#Juan Guillermo Urincho Tinoco.

import math as m
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-1,5)
y=2*(x**2)-(8*x)-11
plt.plot(x,y,linewidth=3,color='b',label='Linea 3')
plt.legend()
plt.title("Grafica B")
plt.xlabel('Ganas de vivir')
plt.ylabel('Semestre')
plt.grid(True)
plt.show()
