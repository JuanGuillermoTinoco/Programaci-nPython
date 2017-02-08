#Proyecto
#Calorias
#Juan Guillermo Urincho Tinoco.

import sys
proyecto="PORQUE BALANCEAR LAS CALORIAS ES CHIDO"
print proyecto.center(100,"=")
print '''

Programas por tu salud y la salud de Mexico'''
raw_input
print'''
Objetivo: Que las personas puedan conocer su requerimiento energetico para que lleven
una vida mas balanceada.
'''
raw_input
print '''
Si a nuestro cuerpo le damos exactamente las calorías que necesita,
mantendremos nuestro peso. Si hay un balance negativo entre lo que
ingerimos y lo que se gasta conlleva a una pérdida de peso, mientras que un
balance positivo conlleva a una subida de peso. Dependiendo de la actividad
física realizada y de los macronutrientes (hidratos de carbono, grasas y
proteínas) ingeridos, ese cambio se traduce en un mayor cambio en el
porcentaje graso del cuerpo o en la musculatura.
'''
n=input('Introduce tu estatura en m: ')
m=input('Introduce tu peso en kg: ')
edad=input('Introduce tu edad: ')
imc=m/(n*n)
#Porcentaje de grasa corporal=pgc
c=raw_input('Sexo(Hombre h/m Mujer): ')
if c=="h" or c=="H":
    pgc=1.20*imc + 0.23*edad -16.2
elif c=="m" or c=="M":
    pgc=1.20*imc + 0.23*edad -5.4
#Grasa Magra=gm
gm=pgc/100
gm1=gm*m
kgm=m-gm1 #Kilos de grasa magra
#Formula de Katch-McArdle:
#El gasto basal es la necesidad energetica de una persona.
#Gasto Basal=gb
gba=21.6*kgm
gb=370+gba
panel='''Actividades fisicas: (Escriba el numero que le corresponda y presione enter.)
Hago muy poco o a veces nada de ejercicio (1)
Deporte de 1-3 veces por semana           (2)
Deporte de 3-5 veces por semana           (3)
Deporte de 6-7 días por semana            (4)
Actividad fisica intensa (dos             (5)
entrenamientos por dia)
'''
eleccion=raw_input(panel)
if eleccion=="1":
    gbf1=gb*1.2
    gbf1n=gbf1*.10
    gbf1t=gbf1+gbf1n
    print 'Su requerimiento calorico total es de: ',gbf1t
elif eleccion=="2":
    gbf2=gb*1.375
    gbf2n=gbf2*.10
    gbf2t=gbf2+gbf2n
    print 'Su requerimiento calorico total es de: ',gbf2t
elif eleccion=="3":
    gbf3=gb*1.55
    gbf3n=gbf3*.10
    gbf3t=gbf3+gbf3n
    print 'Su requerimiento calorico total es de: ',gbf3t
elif eleccion=="4":
    gbf4=gb*1.725
    gbf4n=gbf4*.10
    gbf4t=gbf4+gbf4n
    print 'Su requerimiento calorico total es de: ',gbf4t
elif eleccion=="5":
    gbf5=gb*1.9
    gbf5n=gbf5*.10
    gbf5t=gbf5+gbf5n
    print 'Su requerimiento calorico total es de: ',gbf5t
imc=m/(n*n)
print 'Porcentaje de grasa corporal:',pgc
if imc<16:
    print ("IMC: Delgadez severa.")
elif 16<imc<16.99:
    print ("IMC: Delgadez moderada")
elif 17<imc<18.49:
    print ("IMC: Delgadez leve")
elif 18.5<imc<24.99:
    print ("IMC: Normal")
elif 25<imc<30:
    print ("IMC: Sobrepeso")
elif 30.01<imc<35:
    print ("IMC: Obesidad")
elif 35<imc:
    print ("IMC: Obesidad morbida")

print '''

Cuidate y alimentate bien.'''
