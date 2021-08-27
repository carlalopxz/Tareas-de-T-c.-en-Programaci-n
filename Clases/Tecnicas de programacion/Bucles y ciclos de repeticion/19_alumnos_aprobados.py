# Dadas 6 notas,
# escribir la cantidad de alumnos aprobados (>4)
# condicionados (= 4)
# y suspensos (< 4)

aprobados = 0
condicionados = 0
suspensos = 0
for i in range(6):
    notas = int(input('Ingrese la nota del/la alumno/a \n'))

    if notas > 4:
        aprobados = aprobados + 1
    if notas == 4:
        condicionados = condicionados + 1
    if notas < 4 :
        suspensos = suspensos + 1

print('La cantidad de alumnos aprobados es de: ' + str(aprobados))
print('La cantidad de alumnos condicionados es de: ' + str(condicionados))
print('La cantidad de alumnos suspendidos es de: ' + str(suspensos))