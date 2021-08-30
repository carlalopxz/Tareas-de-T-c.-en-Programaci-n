# Tenemos una lista inicial, lista = [5,3,1,2,4]
# Debemos realizar una lista cuadrado y poner los numeros de la lista inicial elevados al cuadrados

lista = [5,3,1,2,4]

lista_cuadrado = []

for i in lista:
    cuadrado = i ** 2
    lista_cuadrado.append(cuadrado)

print(lista)
print(lista_cuadrado)