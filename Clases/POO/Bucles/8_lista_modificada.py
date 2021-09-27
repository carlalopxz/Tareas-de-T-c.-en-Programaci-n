# Modificar una lista de numeros reales que representan las calificaciones de los alumnos
# de una clase, para sustituir los valores numericos por sus calificaciones alfanumericas
# Suspenso < 6 - Aprobado >= 6.

calificaciones = []
alumno = []
numAlumnos = int(input("Ingrese la cantidad de alumnos:\n"))
for i in range(numAlumnos):
    for j in range(3):
        alumno.append(int(input(f"Ingrese la nota {j}:\n")))
    calificaciones.append(alumno)
    alumno = []
for i in range(len(calificaciones)):
    for j in calificaciones[i]:
        if j >= 6:
            index = calificaciones[i].index(j)
            calificaciones[i][index] =  "Aprobado"
        if j < 6:
            index = calificaciones[i].index(j)
            calificaciones[i][index] = "Suspendido"
print(calificaciones)




