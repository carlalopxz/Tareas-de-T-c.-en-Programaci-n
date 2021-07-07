# Pedir 5 calificaciones de alumnos 
# decir al final si hay algun suspenso.

suspenso = False

for i in range(5):
    nota = int(input('Ingrese la nota del alumno \n'))

    if nota < 6:
        suspenso = True

if suspenso:
    print('Si hay alumnos suspendidos')