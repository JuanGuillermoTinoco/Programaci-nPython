#lABORATORIO. Trabajo en clase. Ejercicio 2. 29/Nov/2016
#Juan Guillermo Urincho Tinoco

n=input('Introduce número de 4 digitos: ')
m=n%1000
md=n-m
mda=md/1000
print mda
c=n-md
cd=c%100
cda=c-cd
cdab=cda/100
print cdab
z=md+cda
d=n-z
dd=d%10
dda=d-dd
ddab=dda/10
print ddab
x=z+dda
u=n-x
print u
suma=mda+cdab+ddab+u
print "La suma de sus digitos es igual a:",suma
