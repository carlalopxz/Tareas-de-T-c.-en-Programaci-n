# Queremos desarrollar una aplicación que nos ayude a gestionar las notas de un centro 
# educativo. Cada grupo (o clase) está compuesto por 5 alumnos. 
# Se pide leer las notas del primer,segundo y tercer trimestre de un grupo. 
# Debemos mostrar al final: la nota media del grupo en cada trimestre, 
# y la nota media del alumno que se encuentra en la posición N (N se lee por teclado).

import random
alumnos = []
trimestres = []
for trimestre in range(3):
    for nota in range(5):
        ingresado = random.randint(1,10)# int(input('Ingrese la nota'))
        print('Ingrese la nota del alumno: '+str(ingresado))
        alumnos.append(ingresado)
    trimestres.append(alumnos)
    alumnos = [] #vacio lista alumnos para ingresar nuevas notas
    print(trimestres)

#trimestres = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
suma = 0
for trimestre in range(1,4):
    for i in trimestres[trimestre -1]:#[1, 2, 3, 4, 5]
        suma = suma + i
    promedio = suma / 5
    print(f'EL promedio del {trimestre}° trimestre es: {promedio}')


alumnoPedido = int(input('De qué alumnos desea calcular el promedio: ')) #0
suma = 0
for i in trimestres: #[10, 7, 1, 9, 3], [6, 3, 7, 4, 2], [4, 2, 9, 9, 1]
    suma = suma + i[alumnoPedido]
alumnoPromedio = suma / 3
print('La nota promedio de ese alumno es: '+str(alumnoPromedio))