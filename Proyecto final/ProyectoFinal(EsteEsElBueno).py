#-*-coding:utf-8 -*-
#Proyecto
#Calorias
#Juan Guillermo Urincho Tinoco.
#Como podra notar en este documento al fin me salieron los graficos con el plato del buen comer.

import sys
import matplotlib.pyplot as plt
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
    gbf=gb*1.2
    gbfn=gbf*.10
    gbft=gbf+gbfn
    print '\n\nSu requerimiento calorico total es de: ',gbft
elif eleccion=="2":
    gbf=gb*1.375
    gbfn=gbf*.10
    gbft=gbf+gbfn
    print '\n\nSu requerimiento calorico total es de: ',gbft
elif eleccion=="3":
    gbf=gb*1.55
    gbfn=gbf*.10
    gbft=gbf+gbfn
    print '\n\nSu requerimiento calorico total es de: ',gbft
elif eleccion=="4":
    gbf=gb*1.725
    gbfn=gbf*.10
    gbft=gbf+gbfn
    print '\n\nSu requerimiento calorico total es de: ',gbft
elif eleccion=="5":
    gbf=gb*1.9
    gbfn=gbf*.10
    gbft=gbf+gbfn
    print '\n\nSu requerimiento calorico total es de: ',gbft

print 'Necesita tomar ',str(((m*2.20462)/2)*0.0295735),'litros de agua al día'

print '\nPorcentaje de grasa corporal:',pgc,'\n'

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

print '\nCuidate y alimentate bien.'
print '''
La grafica te muestra una dieta sugerida de acuerdo a tus resultados. '''

labels = 'Cereales', 'Vegetales', 'Frutas', 'Lacteos','Carnes','Grasas, aceites y dulces'
sizes = [.40,.20,.15,.15,.05,.05]
explode = (0,0,0,0,0,0)
colors=['orange','green','yellow','white','red','brown']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct=lambda(p): '{:.2f} cal'.format(p * gbft/100.0),shadow=True, startangle=90)

ax1.axis('equal')
plt.show()
