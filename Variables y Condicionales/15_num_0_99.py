#Pedir un número de 0 a 99 y mostrarlo escrito.
#Por ejemplo, para 56 mostrar: cincuenta y seis

num = int(input('Digite un numero entre el 0 y el 99 \n'))

if num < 0 or num > 99:
    print('Numero invalido')
elif num == 0:
    print('CERO')
elif num == 1:
    print('UNO')
elif num == 2:
    print('DOS')
elif num == 3:
    print('TRES')
elif num == 4:
    print('CUATRO')
elif num == 5:
    print('CINCO')
elif num == 6:
    print('SEIS')
elif num == 7:
    print('SIETE')
elif num == 8:
    print('OCHO')
elif num == 9:
    print('NUEVE')
elif num == 10:
    print('DIEZ')
elif num == 11:
    print('ONCE')
elif num == 12:
    print('DOCE')
elif num == 13:
    print('TRECE')
elif num == 14:
    print('CATORCE')
elif num == 15:
    print('QUINCE')
elif num == 20:
    print('VEINTE')

decena = num//10
unidad = num - decena*10

if decena == 1:
    if  unidad == 6:
        print('DIECISEIS')
    elif unidad == 7:
        print('DIECISIETE')
    elif unidad == 8:
        print('DIECIOCHO')
    elif unidad == 9:
        print('DIECINUEVE')
elif decena == 2:
    decena = 'VEINTI'
elif decena == 3:
    decena = 'TREINTA'
elif decena == 4:
    decena = 'CUARENTA'
elif decena == 5:
    decena = 'CINCUENTA'
elif decena == 6:
    decena = 'SESENTA'
elif decena == 7:
    decena = 'SETENTA'
elif decena == 8:
    decena = 'OCHENTA'
elif decena == 9:
    decena = 'NOVENTA'

if unidad == 1:
    unidad = 'UNO'
elif unidad == 2:
    unidad = 'DOS'
elif unidad == 3:
    unidad = 'TRES'
elif unidad == 4:
    unidad = 'CUATRO'
elif unidad == 5:
    unidad = 'CINCO'
elif unidad == 6:
    unidad = 'SEIS'
elif unidad == 7:
    unidad = 'SIETE'
elif unidad == 8:
    unidad = 'OCHO'
elif unidad == 9:
    unidad = 'NUEVE'

if num > 15 and num <= 19:
	print('DIECI'+ unidad)

if num > 20 and num <= 29:
	print(decena + unidad)

if num >= 30 and num < 99:
    if(num % 10 == 0):
        print(decena)
    else:
        print(decena + ' y ' + unidad)    
       
    
    
    
    
 