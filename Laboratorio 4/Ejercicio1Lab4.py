#Laboratorio 4. Ejercicio 1
#Juan Guillermo Urincho Tinoco
#Escribe una funcion cuyos parametros de entrada sean:
#(1) el nombre de un archivo de texto, (2) un entero n, y que muestre en la pantalla las primeras n líneas del archivo. Si el archivo no existe, debe mostrarse en la pantalla un mensaje de error.

tn=raw_input('Ingrese Su Archivo De Texto(sin extension): ')
t=tn+".txt"
cumple=0
try:
    archivo=open(t)
    archivo.close()
    cumple=0
except:
    cumple=1
while cumple==1:
    print"Su archivo no se encuentre en el directorio de ejecucion."
    tn=raw_input('Por favor, ingrese otro nombre: ')
    t=tn+".txt"
    try:
        archivo=open(t)
        archivo.close()
        cumple=0
    except:
        cumple=1
tex=open(t, "r")
arc=tex.readline()
N=input("Ingrese el numero de lineas que quiere leer: ")
while N<0:
    print"No hay lineas negativas."
    N=input("Por favor ingrese otro valor: ")
n=range(0,N)
for i in n:
    print ""
    print arc
    arc=tex.readline()
