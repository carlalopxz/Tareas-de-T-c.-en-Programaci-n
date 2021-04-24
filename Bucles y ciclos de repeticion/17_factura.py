#TAREA:Ejercicio.17.Una empresa que se dedica a la venta de desinfectantes necesita un programa para gestionar 
# las facturas. 
# En cada factura figura: el código del artículo, la cantidad vendida en litros y el precio por litro. 
# Se pide de 5 facturas introducidas: 
# Facturación total, 
# cantidad en litros vendidos del artículo 1 
# y cuantas facturas se emitieron de más de$600. 

#############
#Factura 1  #
#Cod: 1     #
#Cant: 50   #
#$/litro: $5#
#############

fac600 = 0
litros = 0
facturacion = 0

for i in range(5):
    facTtal = int(input('Ingrese la facturacion total'))
    litVendidos = int(input('Ingrese la cantidad de litros vendidos'))
    facturacion = facturacion + facTtal
    litros = litros + litVendidos

    if facTtal > 600:
        fac600 = fac600 + 1

print('La facturacion total es de: ' + str(facturacion) + ' pesos.')
print('La cantidad de litros vendidos es de: ' + str(litros) + ' litros')
print('La cantidad de facturas emitidas mayores a $600 son: ' + str(fac600))
