# Tenemos una valija con lo siguiente: Anteojos, Sombrero, Pasaporte, Computadora, Traje, Zapatos.
# Necesitamos separar lo que tenemos en primero, segundo y tercero.
# Imprimir los resultados de las separaciones.

valija = ["Anteojos","Sombrero","Pasaporte","Computadora","Traje","Zapatos"]
primero = []
segundo = []
tercero = []
for i in range(len(valija)):
    if valija[i] == "Traje":
        primero.append(valija[i])
        primero.append(valija[i+1])
    if valija[i] == "Pasaporte":
        segundo.append(valija[i])
        segundo.append(valija[i+1])
    if valija[i] == "Anteojos":
        tercero.append(valija[i])
        tercero.append(valija[i+1])

print(f"Primero: {primero}")
print(f"Segundo: {segundo}")
print(f"Tercero: {tercero}")