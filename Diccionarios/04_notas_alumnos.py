#Ejercicio.4.Crear un programa que nos permita guardar los nombres de los alumnos de una clase 
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardar la información 
# en un diccionario cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas
# de cada alumno.

#Ejemplo
#Materia : Matematica

print('BIENVENIDO AL SISTEMA DE CARGA DE NOTAS')

materia = input('¿De que materia quiere cargar notas? \n A) Matematica \n B) Lengua \n' ).lower()
def carga_Matematica(numeros_alum):
    listado_alumnos_matematica = {}
    notas = []
    for i in range(numeros_alum):
        nombre_alumno = input('¿Cual es el nombre del alumno? \n')
        nota_alumno = int(input(f'¿Cuantas notas de {nombre_alumno} desea ingresar? \n'))
        for j in range(nota_alumno):
            if nombre_alumno not in listado_alumnos_matematica.keys():
                listado_alumnos_matematica[nombre_alumno] = []
            notas_alumnos = int(input('¿Cual es la nota del alumno?'))
            listado_alumnos_matematica[nombre_alumno].append(notas_alumnos)
    print('Los alumnos de matematica y sus respectivas notas: ' + str(listado_alumnos_matematica))

def carga_Lengua(numeros_alum):
    listado_alumnos_matematica = {}
    notas = []
    for i in range(numeros_alum):
        nombre_alumno = input('¿Cual es el nombre del alumno? \n')
        nota_alumno = int(input(f'¿Cuantas notas de {nombre_alumno} desea ingresar? \n'))
        for j in range(nota_alumno):
            if nombre_alumno not in listado_alumnos_matematica.keys():
                listado_alumnos_matematica[nombre_alumno] = []
            notas_alumnos = int(input('¿Cual es la nota del alumno?'))
            listado_alumnos_matematica[nombre_alumno].append(notas_alumnos)
    print('Los alumnos de lengua y sus respectivas notas: ' + str(listado_alumnos_matematica))


if materia[0] == 'a':
    num_alumnos = int(input('Ingrese la cantidad de alumnos que tiene en su clase: '))
    carga_Matematica(num_alumnos)
if materia[0] == 'b':
    num_alumnos = int(input('Ingrese la cantidad de alumnos que tiene en su clase: '))
    carga_Lengua(num_alumnos)