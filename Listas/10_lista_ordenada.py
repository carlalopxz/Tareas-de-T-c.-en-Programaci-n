# Crea una lista de 5 posiciones con números enteros ordenados de menor a mayor. 
# Leer un número N, e insertarlo en la posición adecuada para que la lista 
# continúe ordenada.

listaNum = [1,4,6,8,9]
print(listaNum)
listaNum.append(int(input('Ingrese un número para agregar a la lista')))
#listaNum.sort()
#print(listaNum)

#solucion 2

for i in range(5):
    if listaNum[0] >= listaNum[i]:
        listaNum.insert(i,listaNum[0])
print(listaNum)
