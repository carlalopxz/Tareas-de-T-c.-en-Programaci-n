#Leer los datos correspondientes a dos listas(A y B) de 12 elementos numéricos, 
# y mezclarlos en una tercera lista de la forma: 3 elementos de la lista A, 
# 3 elementos de la lista B, otros 3 elementos de lista A, otros 3 elementos de la lista B, etc.

#Ejemplo:
#Se ingresan estas 2 listas
#listaA = [1,2,3,4,5,6,7,8,9,10,11,12]
#listaB = [1,2,3,4,5,6,7,8,9,10,11,12]
#El resultado es esta lista:
#listaC = [1,2,3,1,2,3,4,5,6,4,5,6,7,8,9,7,8,9,10,11,12,10,11,12]

import random
lista_A = []
for i in range (12):
    lista_A.append(random.randint(1,9))
lista_B = []
for i in range (12):
    lista_B.append(random.randint(1,9))
print (lista_A)
print (lista_B)
lista_C = []
for i in range(0,10,3):
    lista_C.append(lista_A[i: i + 3])
    lista_C.append(lista_B[i: i + 3])
    # 1) i = 0 [0:0+3] [0:3] el 3 no se incluye
    # 2) i = 3 [3:3+3] [3:6] el 6 no se incluye
print(lista_C)