#Escribir un programa que lea una cadena y devuelva un diccionario con la cantidad 
# de veces que aparece cada caracter en la cadena

cadena = input('Ingrese una cadena \n')
print(cadena)
diccLetras = {}
for i in cadena:
    diccLetras[i] = cadena.count(i)
print(diccLetras)