# Crea una lista de 5 posiciones con números enteros ordenados de menor a mayor. 
# Leer un número N, e insertarlo en la posición adecuada para que la lista 
# continúe ordenada.

from random import randint
listaNum = []
for i in range(5):
    listaNum.append(randint(1,99))
listaNum.sort()
print(listaNum)
listaNum.append(int(input('Ingrese un número para agregar a la lista: ')))
#listaNum.sort()
#print(listaNum)

#solucion 2

for i in range(len(listaNum)):
    if listaNum[5] <= listaNum[i]:
        listaNum.insert(i,listaNum[5])
del listaNum[5]
print(listaNum)
