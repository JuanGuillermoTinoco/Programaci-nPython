#Tarea 1.
#Juan Guillermo Urincho Tinoco.

n=int(input("Introduce numero inicial: "))
sum=0
while n<=250:
    if n%5==0:
        n+=3
        print n
        sum+=n
        n-=3
    if n%7==0:
        n+=6
        print n
        sum+=n
        n-=6
    n+=1
print('suma= ',sum)
