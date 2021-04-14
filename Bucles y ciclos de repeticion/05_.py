# Realizar un juego para adivinar un número. 
# Para ello pedir un número N, y luego ir pidiendo números indicando “mayor” o “menor” 
# según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta. 

#Ejemplo:
#EL numero a adivinar = 50
#4
#Muy bajo
#60
#Muy alto
#50
#Acertaste.

num_adivinar = 0

while num_adivinar != 50:
    num_adivinar = int(input('Ingrese un numero \n'))
    if num_adivinar < 50:
        print('El numero a adivinar es mayor al numero ingresado')
    elif num_adivinar > 50:
        print('El numero a adivinar es menor al numero ingresado')
        
else:
    print('El numero ingresado es 50, acertaste!! :D')    