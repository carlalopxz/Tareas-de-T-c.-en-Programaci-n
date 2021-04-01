#EJERCICIO 11

horasUsuario = 0
minutosUsuario = 0 
segundosUsuario = 0 

print('Ingrese la cantidad de horas, minutos y segundos')
horasUsuario = int(input())
minutosUsuario = int(input())
segundosUsuario = int(input())

horas = horasUsuario * 3600
minutos = minutosUsuario * 60
segundos = segundosUsuario / 60

tiempoTotal = horas + minutos + segundos

print('la cantidad de segundos totales es de: ' , tiempoTotal)