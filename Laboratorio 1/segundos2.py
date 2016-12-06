#Trabajo 1. Ejercicio 5
#Juan  Guillermo Urincho Tinoco

num=int(input("Ingrese los segundos: "))
dia=(int(num/86400))
hor=(int((num-(dia*86400))/3600))
minu=(int((num-(dia*86400)-(hor*3600))/60))
seg=(int((num-(dia*86400)-(hor*3600)-(minu*60))))
print(str(dia)+"d "+str(hor)+"h "+str(minu)+"m "+str(seg)+"s")
