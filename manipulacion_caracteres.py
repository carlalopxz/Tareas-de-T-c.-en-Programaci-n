#RAW STRING o CADENA SIN PROCESAR
print(r'Estos son los CD\s de Claudio')
print('Estos son los CD\s de Claudio')

print('--------------------------------------------------')


#CADENA DE LINEA MULTIPLE CON TRIPLE COMILLAS
print('''Querida Alicia:
    El gato de Eva ha sido arrestado por secuestro, robo y extorsión.
Sinceramente,
Roberto.
''')

print('--------------------------------------------------')

#INDICES Y RANGOS DE CADENA
spam = 'Hola Mundo'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])
espuma = spam[0:5]
print(espuma)

print('--------------------------------------------------')

#OPERADORES IN Y NOT IN
valor = 'Hola' in 'Hola Mundo'
print(valor)
valor = 'Hola' in 'Hola'
print(valor)
valor = 'HOLA' in 'Hola Mundo'
print(valor)
valor = '' in 'Spam'
print(valor)
valor = 'gatos' in 'gatos y perros'
print(valor)

print('--------------------------------------------------')


#CADENAS DENTRO DE CADENAS
nombre = 'Alberto'
edad = 4000
print('Hola mi nombre es ' + nombre + '. Tengo ' + str(edad) + ' años. ')
print('Mi nombre es %s. Tengo %s años'%(nombre,edad))
print(f'Mi nombre es {nombre}. El año que viene tendre {edad + 1} años')

print('--------------------------------------------------')


#METODOS DE CADENAS
spam = 'Hola mundo'
print(spam.islower())
print(spam.isupper())
print('HOLA'.isupper())
print('abc12345'.islower())
print('12345'.islower())
print('12345'.isupper())
print('Hola'.upper())
print('Hola'.upper().lower())
print('Hola'.upper().lower().upper())
print('HOLA'.upper())
print('HOLA'.lower().islower())
print('--------------------------------------------------')


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
'''
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
'''
print('--------------------------------------------------')


#METODOS starwith(), endwith() y find()
print('METODOS starwith(), endwith()')
print('Hola mundo!'.startswith('Hola'))
print('Hola mundo!'.endswith('mundo!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hola mundo!'.startswith('Hola mundo!'))
print('Hola mundo!'.endswith('Hola mundo!'))

print('--------------------------------------------------')


print('METODO FIND()')

print('abc123'.find('abc'))
print('abc123'.find('abc',0,-1))
print('abc123'.find('bc',1,3))
print('abc123'.find('123',3,-1))

print('--------------------------------------------------')


#METODOS join() y split()

print('METODOS JOIN() Y SPLIT()')

print(', '.join(['gatos', 'ratas', 'elefantes']))
print(' '.join(['Mi', 'nombre', 'es', 'Simon']))
print('ABC'.join(['Mi', 'nombre', 'es', 'Simon']))
print('Mi nombre es Simon'.split())
print('--------------------------------------------------')
print('MiABCnombreABCesABCSimon'.split('ABC'))
print('MiABCnombreABCesABCSimon'.split('m'))
print('--------------------------------------------------')
