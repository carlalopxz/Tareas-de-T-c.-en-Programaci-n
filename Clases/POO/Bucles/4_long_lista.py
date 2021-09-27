# Definir una funcion que calcule la longitud de una lista o cadena dada

def calculo(tipo):
    cont = 0
    if type(tipo) == list:
        for i in range(len(tipo)):
            cont += 1
    elif type(tipo) == str:
        for i in tipo:
            cont += 1
    return cont

tipo = input("A) Lista B) Cadena\n").lower()

if tipo == "a":
    lista = []
    cantElementos = int(input("Ingrese la cantidad de elementos:\n"))
    for i in range(cantElementos):
        lista.append(input("Ingrese el elemento:\n"))
    print(f"Cantidad de elementos de la lista: {calculo(lista)}")
elif tipo == "b":
    string = input("Ingrese la cadena:\n")
    print(f"Cantidad de caracteres de la cadena: {calculo(string)}")