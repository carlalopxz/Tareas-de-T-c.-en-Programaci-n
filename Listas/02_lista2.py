#Leer 5 números, guardarlos en una lista y mostrarlos en orden inverso al introducido.

lista_num = []

for i in range(5):
    lista_num.append(int(input('Ingrese un número \n')))

print(lista_num[4],lista_num[3],lista_num[2],lista_num[1],lista_num[0])

for i in range(1,len(lista_num)+1):
    print(lista_num[-i], end=',')