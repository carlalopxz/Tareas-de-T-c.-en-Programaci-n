#Leer 10 enteros. Guardar en otra lista los elementos pares de la primera, 
#y a continuaciónlos elementos impares. Realizar dos versiones: 
#una trabajando con los valores y otra trabajando con los índices.

from random import randint 
listaNum = []
for i in range(10):
    listaNum.append(randint(1,50))
print(listaNum)
#Los valores 
listaNueva = []
for j in range(len(listaNum)):
    if listaNum[j] % 2 == 0:
        listaNueva.append(listaNum[j])
for x in range(len(listaNum)):
    if listaNum[x] % 2 != 0:
        listaNueva.append(listaNum[x])
print(listaNueva)
#Los  indices 
listaNew = []
for k in range(10):
    if k % 2 == 0:
        listaNew.append(listaNum[k])
for n in range(10):
    if n % 2 != 0:
        listaNew.append(listaNum[n])
print(listaNew)
