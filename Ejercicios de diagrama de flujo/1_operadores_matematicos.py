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