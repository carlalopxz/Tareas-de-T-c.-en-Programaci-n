#METODOS isX()

print('hola'.isalpha())
print('hola123'.isalpha())
print('hola123'.isalnum())
print('hola'.isalnum())
print('123'.isdecimal())
print(' '.isspace())
print('Este Es Un Titulo'.istitle())
print('Este Es Un Titulo 123'.istitle())
print('Este no Es Un Titulo'.istitle())
print('Este TAMPOCO Es Un Titulo'.istitle())

while True:
    print('Ingresar edad: ')
    edad = input()
    if edad.isdecimal():
        break
    print('Por favor ingrese un numero para la edad')
while True:
    print('Ingrese una contraseña (letras y numeros solamente)')
    password = input()
    if password.isalnum():
        break
    print('La contraseña solo puede tener letras y numeros')