#Pedir una nota de 0 a 10 y mostrarla de la forma: 
#Insuficiente,Regular, Bien, Muy Bien, Sobresaliente.

#10 = sobresaliente
# 8 - 9 = muy bien
# 7 = Bien
# 6 = regular
# 1- 2 - 3 - 4 - 5 = insuficiente 

nota = int(input('Digite una nota de 0 a 10 \n'))

if nota < 0 or nota > 10:
    print('Numeros invalidos')
else:
    if nota == 10:
        print('Sobresaliente')
    elif nota == 9 or nota == 8:
        print('Muy bien')
    elif nota == 7:
        print('Bien')
    elif nota == 6:
        print('Regular')
    else:
        print('Insuficiente')