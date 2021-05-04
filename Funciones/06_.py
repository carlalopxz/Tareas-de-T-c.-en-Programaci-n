# Realizar una funcion que calcule:
# El area --> se le pasará el caracter 'a'
# El volumen --> se le pasará el caracter 'v'
# Le pasamos a la funcion el radio y la altura
# VOLUMEN = pi * radio * altura
# AREA = 2 * pi * radio * altura

import math

def cilindro(radio,altura):
    try:
        a = math.pi * 2 * radio * altura
        v = math.pi * radio * altura 
    except:
        print("Carla zorra")
    else:
        print(f'El area del cilindro es de {a}')
        print(f'El volumen del cilindro es de {v}')

r = int(input('Ingrese el radio del cilindro \n'))
a = int(input('Ingrese la altura del cilindro \n'))

cilindro(r,a)





