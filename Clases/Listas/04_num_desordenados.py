#Leer 10 números enteros, guardarlos en una lista.
#Debemos mostrarlos en el siguiente orden:
#el primero, el último, el segundo, el penúltimo, el tercero, el ante-penúltimo, etc.

#ingreso = [1,2,3,4]
#muestro = [1,4,2,3]

lista_num = []

for num in range(10):
    lista_num.append(int(input('Ingrese un número \n')))

for i in range(5):
    print(lista_num[i],lista_num[-i-1],end=' ')

#En la primera vuelta lista_num[i] vale 0 y lista_num[-i-1] vale -1
#En la segunda vuelta lista_num[i] vale 1 y lista_num[-i-1] vale -2
#Y asi susesivamente 


