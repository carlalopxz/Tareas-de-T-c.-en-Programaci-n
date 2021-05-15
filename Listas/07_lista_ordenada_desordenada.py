#Leer por teclado una serie de 10 números enteros, guardarlos en una lista. 
# La aplicación debe indicarnos si los números están ordenados 
# de forma creciente, despues: decreciente, o si están desordenados.

#Ejemplo:
#ingresada = [1, 1, 1, 2, 2, 3, 6, 9, 9, 9]

# ingresada[0] <= ingresada[1] True
# ingresada[1] <= ingresada[2] True
# ingresada[2] <= ingresada[3] True
# ...
# ingresada[8] <= ingresada[9] True
# Como todo da True, entonces la lista es creciente.

#ingresada = [10,9,8,7,6,7,6,8,9,4]
#False

import random
lista = []
for i in range(5):
    lista.append(random.randint(1,99))
print(lista)
for i in range(0,10,2):
    if lista[i:i + 1] <= lista[i + 1 : i + 2]:
        True
    else:
        False
if lista[i:i + 1] <= lista[i : i + 2]:
    print('La lista está en orden creciente')