#Crear una lista con 10 animales y luego mostrar los animales del indice mayor a 2 y menor a 6.

lista = []
for i in range(10):
    animal = input("Ingrese un animal:\n")
    lista.append(animal)

for animal in range(len(lista)):
    if animal > 2 and animal < 6:
        print(f"Animal:{lista[animal]}")
