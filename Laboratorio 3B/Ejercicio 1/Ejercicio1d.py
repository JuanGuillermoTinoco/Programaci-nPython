#Ejercicio 1 d). Fecha: 02/Dic/16. Laboratorio 3B.
#Juan Guillermo Urincho Tinoco.

import math as m
import matplotlib.pyplot as plt
import numpy as np
t=np.linspace(0,24)
y=(m.e**-0.1*t)*np.sin(2*t)
plt.plot(t,y,linewidth=3,color='grey',label='Linea 4')
plt.legend()
plt.title("Grafica D")
plt.xlabel('Conocimiento')
plt.ylabel('Vida humana')
plt.grid(True)
plt.show()
