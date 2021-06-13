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
listaNum = []
for i in range(10):
    listaNum.append(random.randint(1,9))
print(listaNum)
for i in range(len(listaNum)): #pasa el indice a i de 0 a x
    if listaNum[i] <= listaNum[i+1]: # i = [0,1,2,3,4,5,6,7,8,9]
        creciente = True
    else:
        creciente = False # si el indice primero es menor o igual al indice 
                          #que le sigue devolvemos un creciente true si no un false
        break #al primer false hacemos break
for i in range(len(listaNum)-1):
    if listaNum[i] >= listaNum[i+1]:
        decreciente = True
    else:
        decreciente = False
        break
if creciente: #true
    print('La lista está ordenada de manera creciente.')
if decreciente: #true
    print('La lista está ordenada de manera decreciente.')
if not creciente and not decreciente: #false 
    print('La lista está desordenada.')
