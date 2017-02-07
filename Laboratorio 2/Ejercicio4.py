#Ejercicio 4. Fecha: 25/Nov/16. Practica 2.
#Juan Guillermo Urincho Tinoco.

import math as m
n=input("Numero de lados del poligono (mayor o igual que 3): ")
while n<3:
    print "El numero de lados del poligono debe ser mayor o igual que 3"
    n=input("Numero de lados del poligono (mayor o igual que 3): ")
lados=input("Tamaño del lado: ")
ejex=input("Origen en Eje X(Coordenada en x): ")
ejey=input("Origen en Eje Y(Coordenada en y): ")
while lados<2:
    print "Solo numeros mayores que 1"
    lados=input("Tamaño del lado: ")
def cos(angulodec):
    return m.cos(m.radians(angulodec))
def sin(angulodec):
    return m.sin(m.radians(angulodec))
lin=range(0,n)
angulo=((n-2)*180/n)
mangulo=angulo/2
anguloe=180-angulo
centro=[ejex,ejey]
mlado=lados/2
hip=mlado/cos(mangulo)
x=[]
y=[]
puntos=[]
for i in(lin):
    valorx=round((centro[0]+((cos(i*anguloe)*hip))),2)
    x.append(valorx)
    valory=round((centro[1]+((sin(i*anguloe)*hip))),2)
    y.append(valory)
for i in(lin):
    punto=(x[i],y[i])
    puntos.append(punto)
for i in(lin):
    print "P[" + str(i+1) + "]= ", puntos[i]
