#Definimos un diccionario con los barrios donde viven las siguientes personas:
# - Pedro: lugano
# - Ramiro: Boedo
# - Ricardo: Parque chas
# - Jazmín: Villa Urquiza
# - Andrea: San Cristóbal
# - Laura: Almagro
# Luego eliminar a Pedro y a Jazmín y agregar los siguientes:
# - Marcela: Boedo
# - Roberto: Agronomía

barrios = {}

while True:
  opcion = input("Opcion:\nA) Agregar persona\nB)Eliminar persona\n0 para terminar\n").lower()

  if opcion == "a":
    persona = input("Ingrese el nombre, 0 para terminar:\n")
    if persona == "0":
      for k,v in barrios.items():
        print(f"{k}: {v} ")
      break
    barrio = input(f"Ingrese el nombre del barrio de {persona} :\n")
    barrios[persona] = barrio
  elif opcion == "b":
    eliminar = input("Ingrese el nombre a eliminar, 0 para terminar:\n")
    if eliminar == "0":
      for k,v in barrios.items():
        print(f"{k}: {v} ")
      break
    del barrios[eliminar]
  elif opcion == "0":
    break
