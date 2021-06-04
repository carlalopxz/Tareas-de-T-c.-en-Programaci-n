#Leer 5 números, guardarlos en una lista y a continuación realizar la media de los números positivos, 
# la media de los negativos y contar el número de ceros.

listaNum = []
for i in range(5):
    listaNum.append(int(input('Ingrese un número \n')))

cont_ceros = 0
cont_positivos = 0
cont_negativos = 0
positivos = 0
negativos = 0
for i in listaNum:
    if i > 0:
        positivos = positivos + i
        cont_positivos = cont_positivos + 1
    elif i < 0:
        negativos = negativos + i
        cont_negativos = cont_negativos + 1
    else:
        cont_ceros = cont_ceros + 1

media_positivos = 0
media_negativos = 0

if cont_positivos > 0:
    media_positivos = positivos/cont_positivos
if cont_negativos > 0:
    media_negativos = negativos/cont_negativos

print('La media de los números positivos es de: ' + str(media_positivos))
print('La media de los números negativos es de: ' + str(media_negativos))
print('La cantidad de ceros ingresados es de: ' + str(cont_ceros))
