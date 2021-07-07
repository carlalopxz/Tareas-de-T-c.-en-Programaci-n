#Pedir dos fechas y mostrar el número de días que hay de diferencia. 
#Suponiendo todos los meses de 30 días.

#Ejemplo:
#Fecha1: 1/1/1900
#Fecha2: 5/1/1900
#Diferencia: 4 dias.

#Fecha1: 1/1/1900
#Fecha2: 1/2/1900
#Diferencia: 30 dias

diaA = int(input('Ingrese el dia A \n'))
mesA = int(input('Ingrese el mes A \n'))
añoA = int(input('Ingrese el año A \n'))

diaB = int(input('Ingrese el dia B \n'))
mesB = int(input('Ingrese el mes B \n'))
añoB = int(input('Ingrese el año B \n'))

print('La fecha A ingresada es: ' + str(diaA) + ' - ' + str(mesA) + ' - ' + str(añoA))
print('La fecha B ingresada es: ' + str(diaB) + ' - ' + str(mesB) + ' - ' + str(añoB))

if diaA <= 0 or diaA >= 31 or mesA <= 0 or mesA >= 13 or añoA < 0:
    print('La fecha es invalida')
if diaB <= 0 or diaB >= 31 or mesB <= 0 or mesB >= 13 or añoB < 0:
    print('La fecha es invalida')

if añoA == añoB:
    if mesA == mesB:
        diasC = (diaA - diaB) * (-1) 
        print('Los dias de diferencia son: ' + str(diasC))
    elif añoA == añoB:
        mesC = (mesA - mesB) * 30 * (-1)
        diasC = (diaA - diaB) * (-1)
        diasDiferencia = (mesC + diasC)
        print('Los dias de diferencia son: ' + str(diasDiferencia))
else:
    añoC = (añoA - añoB) * 365 * (-1)
    mesC = (mesA - mesB) * 30 * (-1)
    diasC = (diaA - diaB) * (-1)
    diasDiferencia = (añoC + mesC + diasC) 
    print('Los dias de diferencia son: ' + str(diasDiferencia))



