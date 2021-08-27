#Pedir el día, mes y año de una fecha, decir si es correcta y mostrar la fecha del día siguiente. 
# Suponer que todos los meses tienen 30 días.

#Ejemplo
#1/1/1900 -> 2/1/1900
#31/1/1900 -> 1/2/1900
#31/12/1900 -> 1

dia = int(input('Ingrese un dia \n'))
mes = int(input('Ingrese un mes \n'))
año = int(input('Ingrese un año \n'))

if dia <= 0 or dia >= 31 or mes <= 0 or mes >= 13 or año < 0:
    print('El dato es invalido')
else:
    print(str(dia) + '/' +  str(mes) + '/' + str(año) + ': La fecha es correcta')

dia = dia + 1

if dia > 30:
    dia = 1
    mes = mes + 1
if mes > 12:
    mes = 1
    año = año + 1
    print(str(dia) + '/' + str(mes) + '/' + str(año))
