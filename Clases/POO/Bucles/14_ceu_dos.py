# Crea un script que muestre el nombre de cada pais y sus ciudades con el siguiente formato:
# Las ciudades de Argentina son:
#   - Buenos Aires
#   - Cordoba
#   - Santa fe
# Agregarle a cada pais un dato extra ademas de sus ciudades llamado EsAmericano
# Este valor debe ser true o false
# Hacer que la impresion anterior no muestre paises que no seas americanos 

ceu = [{"Argentina": ["Buenos Aires","Cordoba","Santa fe"],
    "Brasil": ["Brasilia","Rio de Janeiro","Sao Pablo"],
    "Alemania": ["Munich","Hamburgo","Berlin"],
    "Francia": ["Paris","Lion","Marsella"]
}]
for i in ceu:
    for k,v in i.items():
            print(f"Las ciudades de {k}:")
            for values in v:
                print(f"• {values}")

print("\nPunto 2")

for j in ceu:
    for k,v in j.items():
        esAmericano = (input(f"¿El pais {k} es americano? Enter para saltar\n"))
        v.append(bool(esAmericano))

print("\nPunto 3")

for j in ceu:
    for k,v in i.items():
        if v[-1] == True:
            print(f"Las ciudades de {k}:")
            for values in v[0:3]:
                print(f"• {values}")