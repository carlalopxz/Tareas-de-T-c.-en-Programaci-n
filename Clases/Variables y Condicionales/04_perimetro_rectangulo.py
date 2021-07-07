#Tarea 4
# Pedir los lados de un rectangulo y calcular el perimetro. 
# Perimetro = lado 1 + lado 2 + lado 3 + lado 4.

print('Ingrese los valores de los lados de un rectangulo')
ladoA = int(input())
ladoB = int(input())

perimetro = 2*(ladoA + ladoB)

print('El perimetro de un rectangulo es de: ' + str(perimetro))
