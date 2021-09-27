# Tenemos 3 alumnos con notas de 3 materias. 
# Necesitamos saber el promedio de cada materia y luego su promedio general
# Resultado  / Nota /
#  >= 90     /   A  /
# >= 80 < 90 /   B  /
# >= 70 < 80 /   C  /
# >= 60 < 70 /   D  /
# Definan el ejercicio en varias funciones para su mejor resultado
# Al final imprimir los alumnos con su calificacion de letra.

def cargaNotas():
    notas = {}
    notasTotal = []
    for i in range(2):
        for j in range(3):
            materia = input("Ingrese el nombre de la materia:\n").capitalize()
            nota = int(input(f"Ingrese la nota de {materia}:\n"))
            notas[materia] = nota
        notasTotal.append(notas)
        notas = {}
    impresionNotas(notasTotal)
    return notasTotal

def impresionNotas(notas):
    for i in range(len(notas)):
        for k,v in notas[i].items():
            print(f"Nota {i+1}: {k} = {v}")

def impresionMaterias(materias):
  for k,v in materias.items():
    print(f"Promedio de {k}: {v}")

def promedioMaterias(notas):
    #[{Materia:Nota}]
    sumaNotas = 0
    promedioMaterias = {}
    while True:
      materia = input("Ingrese el nombre de la materia que quiere sacar promedio:\n 0 para terminar\n").capitalize()
      if materia == "0":
        break
      for i in notas:
        for k,v in i.items():
          if k == materia:
            sumaNotas += v
          promedioMaterias[materia] = sumaNotas/2
      sumaNotas = 0
    impresionMaterias(promedioMaterias)

def promedioAlumno(notas):
  #[{Materia:Nota}]
  sumaNotas = 0
  promedioAlumno = {}
  while True:
    alumno = input("Ingrese el alumno (indice), E para terminar\n").capitalize()
    if alumno == "E":
      break
    for i in range(len(notas)):
      if int(alumno) == i:
        for v in notas[i].values():
          sumaNotas += v
        promedioAlumno[alumno] = sumaNotas/3
    sumaNotas = 0
  impresionMaterias(promedioAlumno)
  return promedioAlumno

def cambio(alumnos):
  alumnosLetras = {}
  print(alumnos)
  for k,v in alumnos.items():
    if v >= 9:
      alumnosLetras[k] = "A"
    elif v >= 8 and v < 9:
      alumnosLetras[k] = "B"
    elif v >= 7 and v < 8:
      alumnosLetras[k] = "C"
    else:
      alumnosLetras[k] = "D"
    impresionMaterias(alumnosLetras)
notas = cargaNotas()
promedioMaterias(notas)
alumnos = promedioAlumno(notas)
cambio(alumnos)
