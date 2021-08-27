#Escriba un programa que pida  dos numeros y que conteste cual
#es el menor, el mayor o que si son iguales

num1 = int(input("Ingrese el primer numero:\n"))
num2 = int(input("Ingrese el segundo numero:\n"))

if num1 > num2:
    print(f"El numero {num1} es el mayor \nEl numero {num2} es el menor")
elif num2 > num1:
    print(f"El numero {num2} es el mayor \nEl numero {num1} es el menor")
else:
    print(f"Ambos numeros son iguales: {num1} = {num2}")