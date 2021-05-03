#Programar una función que calcule A elevado a la N.

def exponente(a,n):
    total = a ** n
    return total

A = int(input('Ingrese un número A \n'))
N = int(input('Ingrese un número N \n'))

total = exponente(A,N)

print('El total de calcular A elevado a la N es: ' + str(total))