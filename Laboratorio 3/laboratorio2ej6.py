#lABORATORIO. Trabajo en clase. Ejercicio 6. 29/Nov/2016
#Juan Guillermo Urincho Tinoco

n=input('Introduce los años de vida (Humano):')
if n>2:
    s=n-2
    d=s*4+21
    print (str(d)+" años perro.")
elif 2>n>0:
    t=n*10.5
    print (str(t)+" años perro.")
y=2
if y==n:
    r=21
    print (str(r)+" años perro.")
elif 0>n:
    print "Error. (El número es negativo.)"
