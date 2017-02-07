#Ejercicio 2 a). Fecha: 02/Dic/16. Laboratorio 3B.
#Juan Guillermo Urincho Tinoco.

import numpy as np
import matplotlib.pyplot as plt
from math import sin,cos,pi
x=(pi*(np.linspace(0,720,720)))/180
s=[]
v=[]
for i in range(0,len(x)):
	sp=cos(2*x[i])+sin(3*x[i])
	s.append(sp)
for j in range(0,len(x)):
	vp=-2*sin(2*x[j])+3*cos(3*x[j])
	v.append(vp)
plt.figure("Ejercicio 1b")
plt.plot(x,s,linewidth=7,color='g')
plt.legend('Grafica de s(t)')
plt.plot(x,v,linewidth=7,color='r')
plt.legend('Grafica de v(t)')
plt.title("Comparacion de s(x) y v(x)")
plt.xlabel('x=[0,4pi]')
plt.ylabel('f(t) evaluada desde x=0 hasta x=4pi')
plt.grid(True)
plt.show()
