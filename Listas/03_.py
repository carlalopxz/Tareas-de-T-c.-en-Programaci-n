#Leer 5 números, guardarlos en una lista y a continuación realizar la media de los números positivos, 
# la media de los negativos y contar el número de ceros.

listaNum = []
for i in range(5):
    listaNum.append(int(input('Ingrese un número')))

positivos = 0
negativos = 0
for i in listaNum:
    if listaNum > 0:
        positivos = positivos + listaNum
    elif listaNum < 0:
        negativos = negativos + listaNum

print(positivos/5)
print(negativos/5)
