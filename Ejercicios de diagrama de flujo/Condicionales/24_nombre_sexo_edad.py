nombre = input('Ingrese su nombre \n')
edad = int(input('Ingrese su edad \n'))
sexo = input('Ingrese su sexo \n')

if sexo == 'masculino':
    if edad >= 18:
        print('Nombre: ' + nombre + '. Edad: ' + str(edad))
    else:
        print('El usuario es menor de edad')
else:
    print('El usuario es de sexo femenino.')
