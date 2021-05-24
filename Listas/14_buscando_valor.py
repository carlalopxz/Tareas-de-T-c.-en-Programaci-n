# Leer 10 enteros ordenados crecientemente. 
# Leer N y buscarlo en la lista. Se debe mostrar la posición en que se encuentra. 
# Si no está, indicarlo con un mensaje.

#Ejemplo:
#lista = [1,2,3,4,5,6,7,8,9,10]
#buscando = 2
#mostramos "El valor está en la posicion 1"
#buscamos = 11
#mostramos "No se encontró ese valor en la lista"

listaNum = []
for i in range(10):
    listaNum.append(int(input('Ingrese un número entero\n')))
listaNum.sort()
print(listaNum)
numBuscado = int(input('Ingrese el valor que quiere buscar en la lista \n'))
for j in range(len(listaNum)):
        while listaNum[j] == numBuscado:
            print('El número ',numBuscado, ' se encuentra en la posición ',j)
        else:
            print('No se encontro el valor buscado')
            break