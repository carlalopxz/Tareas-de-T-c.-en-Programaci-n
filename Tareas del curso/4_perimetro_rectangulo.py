#Tarea 4
# Pedir los lados de un rectangulo y calcular el perimetro. 
# Perimetro = lado 1 + lado 2 + lado 3 + lado 4.

#Primer perimetro

perimetroA = 0

print('Ingrese los lados de un rectangulo')
lado1 = int(input())
lado2 = int(input())
lado3 = int(input())
lado4 = int(input())

perimetroA = lado1 + lado2 + lado3 + lado4

print('El perimetro del rectangulo es: '+ str(perimetroA))

#2do perimetro

print('Ingrese los valores de los lados de un rectangulo')
ladoA = int(input())
ladoB = int(input())

perimetro = 2*(ladoA + ladoB)

print('El perimetro de un rectangulo es de: ' + str(perimetro))