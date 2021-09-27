# Escribir una funcion sum() y una funcion mult() que sumen y multipliquen respectivamente
# todos los numeros de una lista. 
# Por ejemplo: sum([1,2,3,4]) deberia devolver 10 y mult([1,2,3,4]) deberia devolver 24.

def sum(lista):
    suma = 0
    for i in lista:
        suma += i 
    return suma 

def mult(lista):
    mult = 1
    for i in lista:
        mult *= i
    return mult

listaInput = []
listaCantElementos = int(input("Ingrese la cantidad de elementos de la lista:\n"))
for i in range(listaCantElementos):
    listaInput.append(int(input(f"Elemento {i}:\n")))

print(f"La suma de los elementos de la lista: {sum(listaInput)}")
print(f"La multiplicacion de los elementos de la lista: {mult(listaInput)}")