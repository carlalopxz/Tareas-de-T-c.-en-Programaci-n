# Pide números y mételos en una lista
# Cuando el usuario meta un 0, ya dejaremos de insertar.
# Por ultimo, muestra los numeros ordenados de menor a mayor.
lista = []
insertar = int(input("Ingrese un elemento, 0 para terminar:\n"))
while insertar != 0:
    lista.append(insertar)
    insertar = int(input("Ingrese un elemento, 0 para terminar:\n"))
    if insertar == 0:
        break
print(f"Lista: {lista}")
lista.sort()
print(f"Lista ordenada: {lista}")