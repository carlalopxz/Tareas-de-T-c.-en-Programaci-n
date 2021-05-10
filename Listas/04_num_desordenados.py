#Leer 10 números enteros, guardarlos en una lista.
#Debemos mostrarlos en el siguiente orden:
#el primero, el último, el segundo, el penúltimo, el tercero, el ante-penúltimo, etc.

#ingreso = [1,2,3,4]
#muestro = [1,4,2,3]

lista_num = []

for num in range(10):
    lista_num.append(int(input('Ingrese un número \n')))

print(lista_num[0],lista_num[9],lista_num[1],lista_num[8],lista_num[2],lista_num[7],lista_num[3],lista_num[6],lista_num[4],lista_num[5])

#Se puede hacer con un ciclo de repeticion 