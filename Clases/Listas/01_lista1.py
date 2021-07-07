# Leer 5 números, guardarlos en una lista y mostrarlos en el mismo orden introducido.

lista_num = []
for i in range(5):
    lista_num.append(int(input('Ingrese un número \n')))

print(lista_num)

listaNum2 = []
for i in range(5):
    listaNum2.insert(i,int(input('Ingrese un número \n')))

print(listaNum2)
