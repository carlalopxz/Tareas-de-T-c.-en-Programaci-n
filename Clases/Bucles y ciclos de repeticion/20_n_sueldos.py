# Pedir un numero N,
# Introducir N sueldos 
# Mostrar el sueldo maximo

n = int(input('Ingrese un numero N \n'))

maxSueldo = 0 

for i in range(n):
    sueldos = int(input('Ingrese un sueldo \n'))

    if sueldos > maxSueldo:
        maxSueldo = sueldos

print('El sueldo maximo ingresado es de $',maxSueldo)