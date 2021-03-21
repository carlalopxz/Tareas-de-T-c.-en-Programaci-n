#Tarea 1

print('Hola mundo!')
print('Por favor, ingresa tu nombre')
nombre = input()
print('Bienvenido ' + nombre)

#Tarea 2
#Hacer un programa que te pregunte tu edad y te diga cuantos vas a cumplir este año

'''
edad = input('¿Cuantos años tenes?')
def edadAcumplir(numero1,numero2):
    return numero1 + numero2
    
print('vas a cumplir ' + str(edadAcumplir(int(edad),1)) + ' años')
'''

print('cual es tu edad')
edad = int(input())
print(nombre + ' tenes ' + str(edad) + ' años')
cumpliras = edad + 1
print('Este año cumpliras ' + str(cumpliras))

# Tarea 3
# Pedir el radio de un circulo y calcular su área. A = pi * r^2 

radio = 0 
print('Ingrese un valor de radio')
radio = input()
area = 3.14 * int(radio)**2
print('El área del circulo es de: ' + str(area))

#Tarea 4
# Pedir los lados de un rectangulo y calcular el perimetro. 
# Perimetro = lado 1 + lado 2 + lado 3 + lado 4.

