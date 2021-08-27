# Crear un programa que lea por teclado una lista de 10 números enteros y la desplace 
# una posición hacia abajo/la derecha, manteniendo la misma cantidad de posiciones: 
# el primero pasa a ser el segundo, el segundo pasa a ser el tercero y así sucesivamente.
# El último pasa a ser el primero.

#Ejemplo:
#listaEjemplo = [1,2,3,4,5,6,7,8,9,10]
#resultado = [10,1,2,3,4,5,6,7,8,9]

listaNum=[]
for i in range (10):
    listaNum.append(input('Ingrese un número '))
print(listaNum)
listaNueva=[]
#Para i en un rango de 9, inserto en i lo que vale lista num en i 
for i in range (9):
    listaNueva.insert(i,listaNum[i])
#Inserto en la posicion cero lo que vale lista num en la posicion 9
listaNueva.insert(0,listaNum[9])
print(listaNueva) 

#Clear Screen y Time Module 
import time
lista=[]
for i in range(10):
    lista.append(int(input('Ingrese un número: ')))
print(lista)
while True:
    print("\033[H\033[J") #Limpio pantalla
    #El insert pone en la posicion 0 el valor de la posicion 9
    lista.insert(0,lista[9])
   #Elimina el elemento repetido en la posicion 10
    del lista[10]
    print(lista)
    #Muestra cada 0.1 segundos la lista mutada
    time.sleep(0.1)
