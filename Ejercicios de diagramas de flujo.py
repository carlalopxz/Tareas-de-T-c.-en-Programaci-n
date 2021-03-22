#Acá voy a poner ejemplos que encuentre

#EJERCICIO 1

#Declare dos variables llamadas numero1 y numero2 a las cuales les asigne el valor inicial 0.
#Despues agregue dos funciones input y guarde el valor dentro de mis variables a las cuales les agregue la funcion
#int para que el valor del input pasara de str a int
#Despues defiini las funciones junto con sus argumentos que son mis dos variables y dentro de la funcion 
#Declare una variable llamada resultado a la que le agregue lo que la funcion debe hacer y una funcion int
#Para convertir esos argumentos de srt a int y pedi que la funcion me devuelva la variable resultado.
#Despues fuera de la funcion la llame y puse un print con un str, llamando a la funcion para que se muestre 
#en pantalla.

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