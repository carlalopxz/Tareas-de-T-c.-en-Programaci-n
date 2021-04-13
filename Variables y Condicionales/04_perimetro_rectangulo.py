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

#Resuelve: Sofia Priore

print ('Calcular perímetro de un rectángulo')
print ('Ingrese las medidas de un lado')
lado1 = input()
print ('Ingrese las medidas de otro lado')
lado2 = input()

ladototal1 = int(lado1)*2
ladototal2 = int(lado2)*2
perimetro = ladototal1 + ladototal2
print ('El perímetro es igual a la suma de los lados = ' +str(ladototal1) +'+'+str(ladototal2) )
print ('El perímetro de su rectángulo es= ' +str(perimetro) +'cm')

#Resuelve: Gabriela Balagur

print('Bienvenide!')
print('¿Cuánto mide el lado1 del rectángulo?')
lado1=float(input())
print('¿Cuánto mide el lado2 del rectángulo?')
lado2=float(input())

perimetro = lado1*2 + lado2*2
print('El perímetro es '+str(perimetro))

#Resuelve: Valeria Acosta
print('Bienvenide!')
print('¿Cuánto mide el lado1 del rectángulo?')
lado1=float(input())
print('¿Cuánto mide el lado2 del rectángulo?')
lado2=float(input())
perimetro= lado1*2 + lado2*2
print('El perimetro es' +str(perimetro))

#Resuelve: Santiago Sorroche

print('¿Cuales son los lados de un rectangulo?...')
L1=input() #Es una cadena
L2=input()
L3=input()
L4=input()
Perimetro=int(L1)+int(L2)+int(L3)+int(L4)
print('El perimetro es: '+str(Perimetro))