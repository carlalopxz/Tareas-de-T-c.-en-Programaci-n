# Crear una lista de enteros, inicializarlos según valores aleatorios en el rango 1-20
# y computar la media de los valores, el valor más alto, el más bajo (utilizando listas).
# Utilizar las funciones para generacion de números aleatorios en python.

from random import randint
numAleatorios = []
for i in range(0,20,1):
    numAleatorios.append(randint(1,20))
numAleatorios.sort()

#Media de valores 
suma = 0
contador = 0
for i in numAleatorios:
    suma += i
    contador += 1
print(f"La media de la lista de numeros aleatorios es: {suma/contador}")

#El valor mas alto

print(f"El valor mas alto de la lista de numeros aleatorios es: {numAleatorios[-1]}")

#El valor mas bajo

print(f"El valor mas bajo de la lista de numeros aletorios es: {numAleatorios[0]}")