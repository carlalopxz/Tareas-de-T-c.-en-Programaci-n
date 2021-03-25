#Acá voy a poner ejemplos que encuentre

#EJERCICIO 1

number1 = 0 
number2 = 0 

number1 = int(input('Enter the first number'))
number2 = int(input('Enter the second number'))

def suma(number1, number2):
    resultado = int(number1 + number2)
    return resultado

def resta(number1, number2):
    resultado1 = int(number1 - number2)
    return resultado1

def multiplicacion(number1, number2):
    resultado2 = int(number1 * number2)
    return resultado2

def division(number1, number2):
    resultado3 = int(number1/number2)
    return resultado3

print(str(suma(number1,number2)))
print(str(resta(number1, number2)))
print(str(multiplicacion(number1, number2)))
print(str(division(number1, number2)))

#EJERCICIO 2

gradosC = 0
gradosF = 0 

gradosC = int(input('Ingrese un valor de °C del 0 al 100'))

def conversion(gradosC):
    return (9/5*gradosC)+32

print(str(conversion(gradosC)))

#EJERCICIO 3

import math
print('Digite el valor de los dos catetos')
c1 = int(input())
c2 = int(input())

hipotenusa = math.sqrt((c1)**2 + (c2)**2)

print(str(hipotenusa))

#EJERCICIO 4

longitud = 0

print('Digite el valor del radio')
radio = int(input())

longitud = 2 * 3.14 * radio

print('La longitud de circunferencia es de: ' + str(longitud))

#EJERCICIO 5

baseMenor = 0
baseMayor = 0
altura = 0

print('Digite el valor de la base menor, la base mayor y la altura')
baseMenor = int(input())
baseMayor = int(input())
altura = int(input())

area = ((baseMayor + baseMenor)/2)*altura

print(str(area))

#EJERCICIO 6

x1 = 0
x2 = 0
x3 = 0

n = 3

print('Digite los valores de los 3 números')
x1 = int(input())
x2 = int(input())
x3 = int(input())

mediaAritmetica = (x1 + x2 + x3)/n

print('La media aritmetica es: ' + str(mediaAritmetica))

#EJERCICIO 7

totalCompra = 0 

print('Digite el total de su compra')
totalCompra = int(input())

descuento = (totalCompra*15)/100

precioFinal = (totalCompra - descuento)

print('El precio final de la compra es de: ' + str(precioFinal) + ' pesos')

#EJERCICIO 8

horasTrabajadas = 0
salarioPorHora = 0

print('Digite la cantidad de horas que trabaja y su salario por hora')
horasTrabajadas = int(input())
salarioPorHora = int(input())

salarioDiario = salarioPorHora * horasTrabajadas
salarioMensual = salarioDiario * 31

print('El salario mensual es de: ' + str(salarioMensual))

#EJERCICIO 9

salarioAnterior = 0

print('Digite el valor de su salario')
salarioAnterior = int(input())

aumento = (salarioAnterior*25)/100
salarioFinal = salarioAnterior + aumento 

print('El salario final es de: ' + str(salarioFinal))

#EJERCICIO 10

c1 = 55
c2 = 30
c3 = 15

finalScore = c1 + c2 + c3

print('The final grade is: ' + str(finalScore) + '%')

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

#EJERCICIO 12 

x1 = 0
x2 = 0 
x3 = 0 

print('Digite 3 numeros')
x1 = int(input())
x2 = int(input())
x3 = int(input())

MG = (x1*x2*x3)**(1/3)

print('La media geometrica es de: ', MG)

#EJERCICIO 13 

cantidadMujeres = 0 
cantidadVarones = 0

print('Digite la cantidad de alumnas mujeres y alumnos varones')
cantidadMujeres = int(input())
cantidadVarones = int(input())

cantidadTotalAlumnos = cantidadMujeres + cantidadVarones

porcentajeMujeres = (cantidadMujeres*100) / cantidadTotalAlumnos
porcentajeVarones = (cantidadVarones*100) / cantidadTotalAlumnos

print('el porcentaje de alumnas mujeres es de: ' + str(porcentajeMujeres) + 
    '% y el porcentaje de alumnos varones es de: ' + str(porcentajeVarones) + '%')

#EJERCICIO 14

caraCubo = 0

print('Digite el valor de la cara del cubo')
caraCubo = int(input())

volumen = caraCubo**3
area = 6 * caraCubo**2

print('El volumen del cubo es de: ' + str(volumen) +
    ' y el area es de: ' + str(area))

#EJERCICIO 15

inversion1 = 0
inversion2 = 0
inversion3 = 0

print('Ingrese el valor de las 3 inversiones')
inversion1 = int(input())
inversion2 = int(input())
inversion3 = int(input())

totalInversion = inversion1 + inversion2 + inversion3
porcentaje1 = (inversion1*100) / totalInversion
porcentaje2 = (inversion2*100) / totalInversion
porcentaje3 = (inversion3*100) / totalInversion

print('El porcentaje de la primera inversion es de: ' + str(porcentaje1) + '%')
print('El porcentaje de la segunda inversion es de: ' + str(porcentaje2) + '%')
print('El porcentaje de la tercera inversion es de: ' + str(porcentaje3) + '%')

#EJERCICIO 16

radioEsfera = 0

print('Digite el valor del radio de la esfera')
radioEsfera = int(input())

area = 4 * 3.14 * radioEsfera**2
volumen = (4/3) * 3.14 * radioEsfera**3

print('El area de la esfera es de: ' + str(area))
print('El volumen de la esfera es de: ' + str(volumen))
