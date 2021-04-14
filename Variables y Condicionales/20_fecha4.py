#Pedir dos fechas y mostrar el número de días que hay de diferencia. 
#Suponiendo todos los meses de 30 días.

#Ídem que el ej. 18, con meses de 28, 30 y 31 días. Sin años bisiestos.
#Meses con 30 días: Abril, Junio, Septiembre y Noviembre.
#Meses con 31 días: Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre.
#Meses con 28 días: Febrero (Menos cuando es bisiesto que tiene 29 días).

diaA = int(input('Digite el dia A \n'))
mesA = int(input('Digite el mes A \n'))
añoA = int(input('Digite el mes A \n'))

diaB = int(input('Digite el dia B \n'))
mesB = int(input('Digite el mes B \n'))
añoB = int(input('Digite el año B \n'))

print(f'La fecha A es: {diaA}/{mesA}/{añoA}')
print(f'La fecha B es: {diaB}/{mesB}/{añoB}')

if mesA == 1 or mesA == 3 or mesA == 5 or mesA == 7 or mesA == 8 or mesA == 10 or mesA == 12:
    print('El mes tiene 31 dias') 

    if añoA == añoB and mesA == mesB:
        diaC = diaB - diaA
        print(f'Los dias de diferencia son: {diaC}')
    elif añoA == añoB:
        mesC = (mesB - mesA) * 31
        diasC = diaB - diaA
        diasTotales = mesC + diasC
        print(f'Los dias de diferencia son: {diasTotales}')
    else:
        añoC = (añoB -añoA) * 365
        mesC = (mesB - mesA) * 31
        diasC = diaB - diaA
        diasTotales = mesC + diasC + añoC
        print(f'Los dias de diferencia son: {diasTotales}')
elif mesA == 4 or mesA == 6 or mesA == 9 or mesA == 11:
    print('El mes tiene 30 dias')

    if añoA == añoB and mesA == mesB:
        diaC = diaB - diaA
        print(f'Los dias de diferencia son: {diaC}')
    elif añoA == añoB:
        mesC = (mesB - mesA) * 30
        diasC = diaB - diaA
        diasTotales = mesC + diasC
        print(f'Los dias de diferencia son: {diasTotales}')
    else:
        añoC = (añoB -añoA) * 365
        mesC = (mesB - mesA) * 30
        diasC = diaB - diaA
        diasTotales = mesC + diasC + añoC
        print(f'Los dias de diferencia son: {diasTotales}')
else:
    print('El mes tiene 28 dias')

    if añoA == añoB and mesA == mesB:
        diaC = diaB - diaA
        print(f'Los dias de diferencia son: {diaC}')
    elif añoA == añoB:
        mesC = (mesB - mesA) * 28
        diasC = diaB - diaA
        diasTotales = mesC + diasC
        print(f'Los dias de diferencia son: {diasTotales}')
    else:
        añoC = (añoB -añoA) * 365
        mesC = (mesB - mesA) * 28
        diasC = diaB - diaA
        diasTotales = mesC + diasC + añoC
        print(f'Los dias de diferencia son: {diasTotales}')
    
