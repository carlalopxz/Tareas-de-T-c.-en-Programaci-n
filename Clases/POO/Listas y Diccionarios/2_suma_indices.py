# Crear una lista de 4 numeros para sumar los siguientes indices:
# Indice 0 y 2.
# Indice 1 y 3.

numeros = []

for i in range(4):
    numero = int(input("Ingrese un numero:\n"))
    numeros.append(numero)

print(numeros)

for i in range(len(numeros)):
    if i == 0:
        suma1 = numeros[i] + numeros[i + 2]
    elif i == 1:
        suma2 = numeros[i] + numeros[i + 2]
print(f"Suma de los indices 0 y 2: {suma1}")
print(f"Suma de los indices 1 y 3: {suma2}")