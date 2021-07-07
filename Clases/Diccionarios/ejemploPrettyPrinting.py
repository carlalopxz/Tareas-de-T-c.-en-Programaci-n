import pprint
mensaje = 'Era un día frio de abril, cuando dieron las 12'
contar = {}
for caracter in mensaje:
    contar.setdefault(caracter, 0)
    contar[caracter] = contar[caracter] + 1
pprint.pprint(contar)
print(pprint.pformat(contar),end=' ')