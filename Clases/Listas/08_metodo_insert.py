#Leer mediante el teclado 8 números. Después se debe pedir un número y una posición, 
# insertarlo en la posición indicada, desplazando hacia la derecha las posiciones 
# que le siguen.

#lista.insert(posicion,valor)


listaNum = []
for i in range(8):
    listaNum.append(int(input('Ingrese un número para agregar a la lista \n')))
print(listaNum)
posicion = int(input('Digite la posicion en la que desea agregar el nuevo valor \n'))
valor = int(input('Digite el valor a agregar \n'))
listaNum.insert(posicion,valor)
print(listaNum)
