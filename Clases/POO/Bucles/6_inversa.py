# Definir una funcion inversa() que calcule la inversion de una cadena.
# Por ejemplo: La cadena "Estoy probando" debería devolver la cadena "odnaborp oytse"

def inversa(cadena):
    concatenar = ""
    for i in range(len(cadena)): 
        concatenar += str(cadena[-(i+1)])
    print(concatenar)

cadena = input("Ingrese la cadena a invertir:\n")
inversa(cadena)