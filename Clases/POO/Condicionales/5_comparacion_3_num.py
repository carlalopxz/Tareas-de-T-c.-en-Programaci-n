"""
Escriba un programa que pida 3 numeros y que diga si son los 3
iguales, si hay dos iguales o si son los 3 distintos.
"""

a = int(input("Ingrese un numero a:\n"))
b = int(input("Ingrese un numero b:\n"))
c = int(input("Ingrese un numero c:\n"))

if a == b and b == c:
    print(f"Los 3 numeros son iguales: {a} = {b} = {c}")
elif a == b:
    print(f"{a} = {b} y, {c} != {a} y {b}")
elif a == c:
    print(f"{a} = {c} y, {b} != {a} y {c}")
elif b == c:
    print(f"{b} = {c} y, {a} != {b} y {c} ")
else:
    print("Los 3 numeros son distintos")