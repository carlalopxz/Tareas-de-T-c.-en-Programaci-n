#Pedir un número de 0 a 99 y mostrarlo escrito.
#Por ejemplo, para 56 mostrar: cincuenta y seis

num = int(input('Digite un numero del 0 al 99 \n'))

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



#Ejercicio12.Pedir un número de 0 a 99 y mostrarlo escrito.
#Por ejemplo, para 56 mostrar: cincuenta y seis

nu=int(input('Ingrese numero de 0 a 99: '))

unidad=nu%10 
decena=nu//10
#unidad = nu - decena*10

if(nu==0):
	print('cero')

if(nu==1):
	print('uno')

if(nu==2):
	print('dos')

if(nu==3):
	print('tres')

if(nu==4):
	print('cuatro')

if(nu==5):
	print('cinco')

if(nu==6):
	print('seis')

if(nu==7):
	print('siete')

if(nu==8):
	print('ocho')

if(nu==9):
	print('nueve')

if(nu==10):
	print('diez')

if(nu==11):
	print('once')

if(nu==12):
	print('doce')

if(nu==13):
	print('trece')

if(nu==14):
	print('catorce')

if(nu==15):
	print('quince')

if(nu==20):
	print('veinte')

if (nu>=30) and (nu<99):
	if(decena==3) :
		decena='treinta'
	else:
		if(decena==4) :
			decena='cuarenta'
		else:
			if(decena==5):
				decena='cincuenta'
			else:
				if(decena==6):
					decena='sesenta'
				else:
					if(decena==7):
						decena='setenta'
					else:
						if(decena==8):
							decena='ochenta'
						else:
							if(decena==9):
								decena='noventa'


if (unidad==1) :
    unidad='uno'
else:
    if(unidad==2) :
        unidad='dos'
    else:
        if(unidad==3) :
            unidad='tres'
        else:
            if(unidad==4) :
                unidad='cuatro'
            else:
                if(unidad==5) :
                    unidad='cinco'
                else:
                    if(unidad==6): 
                        unidad='seis'
                    else:
                        if(unidad==7):
                            unidad='siete'
                        else:
                            if(unidad==8):
                                unidad='ocho'
                            else:
                                if(unidad==9):
                                    unidad='nueve'

if (nu>15) and (nu<=19):
	print('dieci'+unidad)

if (nu>20) and (nu<=29):
	print('veinti'+unidad)

if (nu>=30) and (nu<99):
    if(nu%10==0):
        print(decena)
    else:
        print(decena+' y '+unidad)