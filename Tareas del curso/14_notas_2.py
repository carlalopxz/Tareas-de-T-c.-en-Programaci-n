#Ejercicio11.Pedir una nota numérica entera entre 0 y 10, y mostrar dicha nota de la forma: 
#cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez.

num = int(input('Digite un numero del 0 al 10 \n'))

if num < 0 or num > 10:
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
else:
    print('DIEZ')