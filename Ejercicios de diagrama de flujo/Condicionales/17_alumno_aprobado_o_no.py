print('Digite las 3 notas')
n1 = int(input())
n2 = int(input())
n3 = int(input())

suma = n1 + n2 + n3
promedioNota = suma / 3

if promedioNota >= 10.5:
    print('El alumno esta aprobado')
else:
    print('El alumno esta desaprobado')