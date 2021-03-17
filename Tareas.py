#Tarea1

print('Hola mundo!')
print('Por favor, ingresa tu nombre')
nombre = input()
print('Bienvenido ' + nombre)

#Tarea2
#Hacer un programa que te pregunte tu edad y te diga cuantos vas a cumplir este año

edad = input('¿Cuantos años tenes?')
def edadAcumplir(numero1,numero2):
    return numero1 + numero2
    
print('vas a cumplir ' + str(edadAcumplir(int(edad),1)) + ' años')

# Lo que hice fue guardar el input de ¿cuantos años tenes? dentro de una variable llamada edad, 
# definí una función y la llamé "edadAcumplir", le pusé dos argumentos: numero1 y numero2,
# le pedí a la funcion con un return que me devolviera la suma de ambos argumentos,
# y con un print mostré en pantalla la edad que va a cumplir el usuario, le agregue
# una funcion int() para cambiar el srt de la variable edad, llame a la funcion y a esta
# le agregue la funcion srt() para cambiar el numero dentro de la funcion a un string y asi
# poder concatenar el string con el mensaje que queria mostrar

#Tarea3
