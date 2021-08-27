# Pedir 10 numeros 
# mostrar al final si se han introducido numeros negativos

negativos = 0
for i in range(10):
    num = int(input('Ingrese un numero'))

    if num < 0:
        negativos = negativos + 1
if num < 0:
    print('Se han introducido ' + str(negativos) + ' numeros negativos')
else:
    print('No se han introducido numeros negativos')


#solucion 2

negativoIntroducido = False
for i in range(10):
    num = int(input('Ingrese un numero'))
    if num < 0 :
        negativoIntroducido = True

if negativoIntroducido:
    print('Ingreso un numero negativo')