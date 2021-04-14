# Pedir números hasta que se teclee uno negativo, 
# y mostrar cuántos números se han introducido. 

num = int(input('Ingrese un numero \n'))

cont = 0

while num >= 0:
    cont = cont + 1
    num = int(input('Ingrese un numero \n'))

print('El numero ingresado es negativo')
print('La cantidad de numeros ingresados es: ' + str(cont))
