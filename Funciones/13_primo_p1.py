#Diseña una función que decida si un número es primo. 

#A. Programar una función que nos diga si A es divisible por B. 
# 14 - 2
# 14 % 2 == 0
# 14 es divisible por 2

def divisiblePor(A,B):
    if A % B == 0:
        print(f'El número {A} es divisible por {B}')
    else:
        print(f'El número {A} no es divisible por {B}')

numA = int(input('Ingrese el primer numero - A \n'))
numB = int(input('Ingrese el segundo numero - B \n'))

divisiblePor(numA,numB)

#B. Programar una función que aumente en 1 una variable global contadora 

def aumentar():
    global contador
    contador = contador + 1

contador = 0

print(contador)
aumentar()
print(contador)

