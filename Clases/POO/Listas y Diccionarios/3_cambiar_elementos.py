# Crear la siquiente lista de animales: ["Mono","Elefante","Tigre","Oso"].
# Reemplazar el tigre por un perro.
# Reemplazar oso por gato

lista = ["Mono","Elefante","Tigre","Oso"]

for i in range(len(lista)):
    if lista[i] == "Tigre":
        lista[i] = "Perro"
    if lista[i] == "Oso":
        lista[i] = "Gato"

print(lista) 