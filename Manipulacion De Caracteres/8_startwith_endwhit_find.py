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