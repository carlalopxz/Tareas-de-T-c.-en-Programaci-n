#EJERCICIO 13 

cantidadMujeres = 0 
cantidadVarones = 0

print('Digite la cantidad de alumnas mujeres y alumnos varones')
cantidadMujeres = int(input())
cantidadVarones = int(input())

cantidadTotalAlumnos = cantidadMujeres + cantidadVarones

porcentajeMujeres = (cantidadMujeres*100) / cantidadTotalAlumnos
porcentajeVarones = (cantidadVarones*100) / cantidadTotalAlumnos

print('el porcentaje de alumnas mujeres es de: ' + str(porcentajeMujeres) + 
    '% y el porcentaje de alumnos varones es de: ' + str(porcentajeVarones) + '%')