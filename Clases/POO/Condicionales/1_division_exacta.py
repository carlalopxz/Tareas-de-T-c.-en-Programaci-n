"""
Escriba un programa que pida dos numeros enteros y que calcule
su division, escribiendo si la division es exacta o no.
"""

num1 = int(input("Ingrese el primer numero:\n"))
num2 = int(input("Ingrese el segundo numero:\n"))
try:
    if num2 != 0:
        division = num1 / num2
    if num1 % num2 == 0:
        print(f"El resultdo de la division {division} es exacto")
    else:
        print(f"El resultado de la division {division} no es exacto")
except:
    print("Se trato de dividir por cero")
