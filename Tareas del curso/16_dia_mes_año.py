#Pedir el día, mes y año de una fecha e indicar si la fecha es correcta. 
#Suponiendo todos los meses de 30 días.

dia = int(input('Ingrese un dia \n'))
mes = int(input('Ingrese un mes \n'))
año = int(input('Ingrese un año \n'))

if dia <= 0 or dia >= 31 or mes <= 0 or mes >= 13 or año < 0:
    print('El dato es invalido')
else:
    1 >= dia <= 30
    1 >= mes <= 12
    print(str(dia) + '/' +  str(mes) + '/' + str(año) + ': La fecha es correcta')