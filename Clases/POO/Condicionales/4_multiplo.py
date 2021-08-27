#Escriba un programa que pida dos numeros enteros.
#Calcule si el mayor es multiplo del menor. 

a = int(input("Ingrese un numero a: \n"))
b = int(input("Ingrese un numero b: \n"))

if a > b:
    multiplo = a % b 
    if multiplo == 0:
        print(f"El numero {a} es multiplo de {b}")
    else:
        print("No es multiplo")
else:
    multiplo = b % a
    if multiplo == 0:
        print(f'El numero {b} es multiplo de {a}')
    else:
        print("No es multiplo")