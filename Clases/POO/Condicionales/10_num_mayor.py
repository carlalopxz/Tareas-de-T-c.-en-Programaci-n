#Elabora un algoritmo para leer 3 números enteros diferentes entre si, y determinar el número mayor de los 3.

a = int(input("Ingrese un numero a:\n"))
b = int(input("Ingrese un numero b:\n"))
c = int(input("Ingrese un numero c:\n"))

if a > b and b > c:
    print(f"El numero mayor es {a}: {a} - {b} - {c}")
elif b > a and a > c:
    print(f"El numero mayor es {b}: {b} - {a} - {c}")
else:
    print(f"El numero mayor es {c}: {c} - {a} - {b}")