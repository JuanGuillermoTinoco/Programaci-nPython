#Trabajo 1. Ejercicio 6.
#Juan Guillermo Urincho Tinoco.

n=input('Introduce tu estatura en m: ')
m=input('Introduce tu peso en kg: ')
imc=m/(n*n)
print "IMC=",imc
if imc<16:
    print ("Delgadez severa.")
elif 16<imc<16.99:
    print ("Delgadez moderada")
elif 17<imc<18.49:
    print ("Delgadez leve")
elif 18.5<imc<24.99:
    print ("Normal")
elif 25<imc<30:
    print ("Sobrepeso")
elif 30.01<imc<35:
    print ("obesidad")
elif 35<imc:
    print ("Obesidad morbida")
