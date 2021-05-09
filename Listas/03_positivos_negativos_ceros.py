#Leer 5 números, guardarlos en una lista y a continuación realizar la media de los números positivos, 
# la media de los negativos y contar el número de ceros.

listaNum = []
for i in range(5):
    listaNum.append(int(input('Ingrese un número \n')))
    
cont = 0
positivos = 0
negativos = 0
for i in listaNum:
    if i > 0:
        positivos = positivos + i
    elif i < 0:
        negativos = negativos + i
    else:
        cont = cont + 1

print('La media de los números positivos es de: ' + str(positivos/5))
print('La media de los números negativos es de: ' + str(negativos/5))
print('La cantidad de ceros ingresados es de: ' + str(cont))
