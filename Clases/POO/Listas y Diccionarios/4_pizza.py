#Crear una lista vacia, luego ir agregando los ingredientes para hacer una pizza.
# Los ingredientes son los siguientes:
# - Harina - Levadura - Agua - Sal - Salsa de tomate - Queso.
#El programa debe mostrar los ingredientes y la cantidad de ingredientes que se utilizó.

ingredientes = []

numIngredientes = int(input("¿Cuantos ingredientes desea agregar?\n")) 

for i in range(numIngredientes):
    ingrediente = input(f"Ingrese el ingrediente {i}:\n")
    ingredientes.append(ingrediente)

print(f"Lista de ingredientes: {ingredientes}")
print(f"La cantidad de ingredientes es: {numIngredientes}")