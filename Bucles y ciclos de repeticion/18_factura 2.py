# Igual que el anterior, pero suponiendo que no se introduce el precio por litro. 
# Solo existen tres productos con precios:
# 1- $0,6 /litro,
# 2- $3 /litro
# 3- $1,25 /litro. 

fac600 = 0
litros = 0
factTotal = 0
for i in range(5):
    print('Factura n°:', i+1)
    codFac = int(input('Ingrese el codigo de la factura: '))
    litVendidos = int(input('Ingrese la cantidad de litros vendidos: '))

    litros = litros + litVendidos

    if codFac == 1:
        factTotal = litVendidos * 0.6

    if codFac == 2:
        factTotal = litVendidos * 3

    if codFac == 3:
        factTotal = litVendidos * 1.25

    if factTotal > 600:
        fac600 = fac600 + 1

if codFac == 1:
    print('Total de ventas codigo facturacion 1:')
    print('La facturacion total del cod. 1 es de: ' + str(factTotal) + ' pesos.')

if codFac == 2:
    print('Total de ventas codigo de facturacion 2:')
    print('La facturacion total del cod. 2 es de: ' + str(factTotal) + ' pesos.')

if codFac == 3:
    print('Total de ventas codigo de facturacion 3:')
    print('La facturacion total del cod. 3 es de: ' + str(factTotal) + ' pesos.')



print('La cantidad de litros vendidos es de: ' + str(litros) + ' litros')
print('La cantidad de facturas emitidas mayores a $600 son: ' + str(fac600))