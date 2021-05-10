# Leer por teclado dos listas de 10 números enteros y mezclarlas en una tercera de la forma: 
# el 1º de A, el 1º de B, el 2º de A, el 2º de B, etc.

import random
 
lista1 = []
for i in range (10):
    lista1.append(random.randint(1,100))
#Hacemos un for donde pasamos 10 veces haciendo una lista con numeros aleatorios entre 0 y 100
    
lista2 = []
for i in range (10):
    lista2.append(random.randint(1,100))
#Hacemos lo mismo que en el for anterior pero con la lista 2

print (lista1)
print (lista2)
#Imprimimos ambas listas

lista3 = []
for i in range (10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])
#Hacemos un for que pase 10 veces y vamos agregando a la lista 3 primero lo que vale i en lista 1 
#y despues lo que vale i en lista 2

print (lista3)
#Imprimimos la lista 3