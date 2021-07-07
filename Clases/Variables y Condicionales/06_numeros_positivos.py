#TAREA 6 
#Pedir un número e indicar si es positivo o negativo.

print('Digite un número')
numero = input()

if int(numero) > 0:
    print('El número es positivo: ' + numero)
elif int(numero) < 0:
    print('El número es negativo:' + numero)
else: 
    print('El número ingresado es cero')