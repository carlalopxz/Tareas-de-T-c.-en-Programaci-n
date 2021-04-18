# Pedir números hasta que se introduzca un 0, 
# mostrar la suma de todos los números introducidos, y calcular la media. 

#promedio = la suma de los numeros / cantidad de numeros num = int(input('Ingrese un numero \n'))

'''
num = 1
while num !=0:
    num = int(input('Ingrese un numero'))
'''
suma = 0
cant = 0
while True:
    num = int(input('Ingrese un numero'))
    if num == 0:
        break
    suma = suma + num
    cant = cant + 1
print('Suma de los numeros: '+str(suma))
print('Promedio de los numeros: '+str(int(suma/cant)))

