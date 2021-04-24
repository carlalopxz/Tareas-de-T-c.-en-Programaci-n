#Pedir 10 números.
#Mostrar la media de los números positivos,
# la media de los números negativos
# y la cantidad de ceros ingresados. 

#Promedio = Suma / Cantidad

sumaPos = 0
cantPos = 0
sumaNeg = 0
cantNeg = 0
cantCeros = 0
for i in range(10):
    num = int(input('Ingrese un número: '))
    if num > 0:
        sumaPos = sumaPos + num #Acumulo positivos
        cantPos = cantPos + 1 #Cuento positivos
    elif num < 0 :
        sumaNeg = sumaNeg + num #Acumulo negativos
        cantNeg = cantNeg + 1 #Cuento negativos
    else:
        cantCeros = cantCeros + 1 #Cuento los ceros

if cantPos > 0:
    promedioPos = sumaPos / cantPos
    print('El promedio de los positivos es: '+str(promedioPos))
else:
    print('No se ingresaron numeros positivos.')

if cantNeg > 0:
    promedioNeg = sumaNeg / cantNeg
    print('El promedio de los negativos es: '+str(promedioNeg))
else:
    print('No se ingresaron numeros negativos.')

print('La cantidad de ceros ingresados es: '+str(cantCeros))

