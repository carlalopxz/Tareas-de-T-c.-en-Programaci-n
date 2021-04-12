#Ejercicio19 .Ídem que el ej.17, con meses de 28, 30 y 31 días. 
# Sin años bisiestos. (suponer que febrero tiene siempre 28 días y el resto 30 o 31 según corresponda)

#Meses con 30 días: Abril, Junio, Septiembre y Noviembre.
#Meses con 31 días: Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre.
#Meses con 28 días: Febrero (Menos cuando es bisiesto que tiene 29 días).

dia = int(input('Ingrese un dia \n'))
mes = int(input('Ingrese un mes \n'))
año = int(input('Ingrese un año \n'))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes ==8 or mes == 10 or mes == 12:
    print('El mes tiene 31 dias')
    if dia < 31:
        dia = dia + 1
        print(f'Mañana sera: {dia}/{mes}/{año}')
    elif dia == 31 and mes < 12:
        mes = mes + 1
        print(f'Mañana sera: {dia}/{mes}/{año}')
    elif dia == 31 and mes == 12:
        año = año + 1
        print(f'Mañana sera: 1/1/{año}')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print('El mes tiene 30 dias')
    if dia < 30:
        dia = dia + 1
        print(f'Mañana sera: {dia}/{mes}/{año}')
    elif dia == 30 and mes < 11:
        mes = mes + 1
        print(f'Mañana sera: {dia}/{mes}/{año}')
    elif dia == 30 and mes == 11:
        mes = mes + 1
        print(f'Mañana sera: {dia}/{mes}/{año}')
else:
    print('El mes tiene 28 dias')
    if dia < 28:
        dia = dia + 1
        print(f'Mañana sera: {dia}/{mes}/{año}')
    elif dia == 28:
        print(f'Mañana sera:  1/3/{año}')


    
     