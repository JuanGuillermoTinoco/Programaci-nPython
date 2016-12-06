#lABORATORIO. Trabajo en clase. Ejercicio 3. 29/Nov/2016
#Juan Guillermo Urincho Tinoco

n=input('Introduce número de 3 digitos: ')
m=n%100
md=n-m
mda=md/100
c=n-md
cd=c%10
cda=c-cd
cdab=cda/10
z=md+cda
d=n-z
list=[mda,cdab,d]
g=sorted(list)
print "Números ordenados de menor a mayor:",g
