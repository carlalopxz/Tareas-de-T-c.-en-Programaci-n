# Diseñar una función que tenga como parámetros dos números, y que calcule el máximo entre 2 numeros.
# Ejercicio3.Ídem una versión que calcule el máximo de 3 números.

def numMax(num1,num2,num3):

    if num1 and num2 > num3:
        if num1 > num2:
            maximo = num1
            print('El maximo es: ' + str(maximo))
        else:
            maximo = num2
            print('El maximo es: ' + str(maximo))
    elif num3 > num1 and num2:
        maximo = num3
        print('El maximo es: ' + str(maximo))
    else:
        maximo = print('Los numeros son iguales ')

num1 = int(input('Ingrese el primer numero \n'))
num2 = int(input('Ingrese el segundo numero \n'))
num3 = int(input('Ingrese el tercer numero \n'))

numMax(num1,num2,num3)


