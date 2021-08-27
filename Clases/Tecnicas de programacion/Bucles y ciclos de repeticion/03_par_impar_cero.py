# Leer números hasta que se introduzca un 0. Para cada uno indicar si es par o impar.
# Pedir un numero e indicar si es par o impar. 
# Repetir el proceso hasta que se introduzca un 0.

num = int(input('Digite un número \n'))

while num != 0:
    if num  % 2 == 0:
        print('El numero ' + str(num) + ' es par')
    else:
        print('El numero ' + str(num) + ' es impar')
    num = int(input('Digite un número \n'))
print('El numero ingresado es ' + str(num))