# Escribir un programa que pida un número por teclado y que cree un diccionario 
# cuyas claves sean desde el número 1 hasta el número indicado, 
# y los valores sean los cuadrados de las claves.

num = int(input('Ingrese un número \n'))
diccionario = {}
for i in range(1,num + 1):
    diccionario[i] = i**2
print(diccionario)