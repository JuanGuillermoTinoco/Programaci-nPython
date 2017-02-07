#Ejercicio 2 d). Fecha: 02/Dic/16. Laboratorio 3B.
#Juan Guillermo Urincho Tinoco.

import numpy as np
import matplotlib.pyplot as plt
from math import pi
x=(pi*(np.linspace(0,360,360)))/180
f=(1+(2*np.sin(x)))*(np.cos(x))
g=(1+(2*np.sin(x)))*(np.sin(x))
plt.figure("Ejercicio 1d")
plt.plot(x,f,linewidth=5,color='pink',label='Grafica de X(t)')
plt.legend()
plt.plot(x,g,linewidth=6,color='red',label='Grafica de Y(t)')
plt.legend()
plt.title("Comparacion de X(t) y Y(t)")
plt.xlabel('x=[0,2pi]')
plt.ylabel('X(t) y Y(t)')
plt.grid(True)
plt.show()
