# Pedir 5 numeros
# Indicar si alguno es multiplo de 3

multiplode3=0
for i in range (5):
    num=int(input('Indique un número: '))
    if num % 3==0:
        multiplode3=multiplode3+1
print('Los números múltiplo de 3 son: '+str(multiplode3))

#Con variable bandera

multiplode3=False
for i in range (5):
    num=int(input('Indique un número: '))
    if num % 3==0:
        multiplode3=True

if multiplode3:
    print('Se introdujo algun multiplo de 3')