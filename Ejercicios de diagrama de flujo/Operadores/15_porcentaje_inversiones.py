#EJERCICIO 15

inversion1 = 0
inversion2 = 0
inversion3 = 0

print('Ingrese el valor de las 3 inversiones')
inversion1 = int(input())
inversion2 = int(input())
inversion3 = int(input())

totalInversion = inversion1 + inversion2 + inversion3
porcentaje1 = (inversion1*100) / totalInversion
porcentaje2 = (inversion2*100) / totalInversion
porcentaje3 = (inversion3*100) / totalInversion

print('El porcentaje de la primera inversion es de: ' + str(porcentaje1) + '%')
print('El porcentaje de la segunda inversion es de: ' + str(porcentaje2) + '%')
print('El porcentaje de la tercera inversion es de: ' + str(porcentaje3) + '%')