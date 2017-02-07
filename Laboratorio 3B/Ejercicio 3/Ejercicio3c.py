#Ejercicio 3 c). Fecha: 02/Dic/16. Laboratorio 3B.
#Juan Guillermo Urincho Tinoco.

import numpy as np
import matplotlib.pyplot as plt
from math import pi
t=(pi*(np.linspace(0,360,360)))/180
x=np.sin(3*t)
y=np.cos(4*t)
plt.figure("Ejercicio 3c")
plt.plot(t,x,linewidth=5,color='red',label='Grafica de X(t)')
plt.legend()
plt.plot(t,y,linewidth=7.2,color='green',label='Grafica de Y(t)')
plt.legend()
plt.title("X vs Y")
plt.xlabel('x=[0,2pi]')
plt.ylabel('X(t) y Y(t)')
plt.grid(True)
plt.show()
