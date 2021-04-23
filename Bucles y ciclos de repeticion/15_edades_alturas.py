#Dadas las edades y alturas de 5 alumnos, 
# mostrar la edad y la estatura media, 
# la cantidad de alumnos mayores de 18 años, 
# y la cantidad de alumnos que miden más de 1.75m. (175cm)

edadMedia = 0

alturaMedia = 0

mayoresA18 = 0
mayoresDe175 = 0

for i in range(5):
    edades = int(input('Ingrese la edad \n'))
    alturas = float(input('Ingrese las estaturas \n'))
    
    edadMedia = edadMedia + edades
    
    alturaMedia = alturaMedia + alturas

    if edades > 18:
        mayoresA18 = mayoresA18 + 1

    if alturas > 1.75:
        mayoresDe175 = mayoresDe175 + 1

print('La edad media es de: ' + str(edadMedia/5))
print('La estatura media es de: ' + str(alturaMedia/5))

print('La cantidad mayores a 18 son: ' + str(mayoresA18))
print('La cantidad mayores a 1.75 son: ' + str(mayoresDe175))
