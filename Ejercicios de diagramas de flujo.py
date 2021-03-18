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

numero1 = 0 
numero2 = 0 

numero1 = int(input('Digite el primer número'))
numero2 = int(input('Digite el segundo número'))

def suma(numero1, numero2):
    resultado = int(numero1 + numero2)
    return resultado

def resta(numero1, numero2):
    resultado1 = int(numero1 - numero2)
    return resultado1

def multiplicacion(numero1, numero2):
    resultado2 = int(numero1 * numero2)
    return resultado2

def division(numero1, numero2):
    resultado3 = int(numero1/numero2)
    return resultado3

print(str(suma(numero1,numero2)))
print(str(resta(numero1, numero2)))
print(str(multiplicacion(numero1, numero2)))
print(str(division(numero1, numero2)))

#EJERCICIO 2

gradosC = 0
gradosF = 0 

gradosC = int(input('Ingrese un valor de °C del 0 al 100'))

def conversion(gradosC):
    return (9/5*gradosC)+32

print(str(conversion(gradosC)))