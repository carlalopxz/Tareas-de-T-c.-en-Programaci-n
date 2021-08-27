#Escriba un programa que pida el año actual y un año x.
#Que diga cuantos años han pasado desde ese año o cuantos
#Faltan para llegar al mismo.

añoActual = int(input("Ingrese el año actual:\n"))
añoX = int(input("Ingrese un año x:\n"))

if añoActual > añoX:
    añosPasados = añoActual - añoX
    print(f"Han pasado desde el {añoX} hasta el {añoActual}, {añosPasados} años")
else:
    añosQueFaltan = añoX - añoActual
    print(f"Faltan para llegar al año {añoX}, {añosQueFaltan} años")