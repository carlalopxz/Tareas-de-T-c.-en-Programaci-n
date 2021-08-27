#JUSTIFICACION DE TEXTO 
print('METODOS RJUST(), LJUST() Y CENTER()')

print('Hola'.rjust(10))
print('Hola'.rjust(20))
print('Hola Mundo'.rjust(20))
print('Hola'.ljust(10))
print('--------------------------------------------------')
print('Hola'.rjust(20,'*'))
print('Hola'.ljust(20,'-'))
print('--------------------------------------------------')
print('METODO CENTER()')
print('Hola'.center(20))
print('Hola'.center(20, '='))
print('--------------------------------------------------')
def imprimirPicnic(elementosDict, anchoIzq, anchoDer):
    print('Elementos del Picnic'.center(anchoIzq + anchoDer, '-'))
    for k, v in elementosDict.items():  
        print(k.ljust(anchoIzq, '.') + str(v).rjust(anchoDer))
elementosPicnic = {'sanguches': 4, 'manzanas': 12, 'vasos': 4, 'galletitas': 8000}
imprimirPicnic(elementosPicnic, 12, 5)
print('--------------------------------------------------')
imprimirPicnic(elementosPicnic, 20, 6)
