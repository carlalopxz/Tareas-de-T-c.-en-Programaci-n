#Pedir 10 sueldos. Mostrar su suma y cuantos hay mayores de $1000.

suma = 0
cant = 0
for i in range(1,11):
    sueldo = int(input('Ingrese su sueldo \n'))
    suma = suma + sueldo

    if sueldo > 1000:
        cant = cant + 1

print('La suma de todos los sueldos es ' + str(suma) + ' pesos.')
print('La cantidad de sueldos mayores a $1000 es: ' + str(cant))