#Crear 2 listas con 10 números enteros ordenados de menor a mayor. 
# Copiar los valores de ambas listas en una tercera, de forma que sigan 
# ordenados de menor a mayor.
#Ejemplo:
#lista1 = [10,30,50,70,90,110,130,150,170,190]
#lista2 = [2,4,6,8,10,12,14,16,18,20]
#lista3 = [2,4,6,8,10,10,12,14,16,18,20,30,50,70,90,110,130,150,170,190]

lista1 = []
for i in range(10):
    lista1.append(int(input('Ingrese un número entero\n')))
print(lista1)
lista2 = []
for j in range(10):
    lista2.append(int(input('Ingrese un número entero\n')))
print(lista2)
lista3 = lista1 + lista2
lista3.sort()
print(lista3)
