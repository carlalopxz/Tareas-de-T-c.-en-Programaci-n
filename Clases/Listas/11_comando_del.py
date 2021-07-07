# Leer por teclado una lista de 10 elementos numéricos enteros, 
# y una posición (entre 0 y 9). Eliminar el elemento situado en la posición dada 
# sin dejar una posición vacía en la lista.

listaNum = []
for i in range(10):
    listaNum.append(int(input('Ingrese un número \n')))
print(listaNum)
pos = int(input('Ingrese la posición a eliminar \n'))
del listaNum[pos]
print(listaNum)