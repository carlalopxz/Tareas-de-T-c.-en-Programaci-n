# Tenmos residentes en una ciudad, hombres = 4500, mujeres = 5500 y  niños = 3000
# Crear un diccionario con los datos brindados, para luego mostrar la cantidad de habitantes que hay
# Entre mujeres y niños

residentes = {}
hombres = int(input("Cuantos residentes hombres hay:\n"))
mujeres = int(input("Cuantas residentes mujeres hay:\n"))
niños = int(input("Cuantos residentes niños hay:\n"))

residentes["Hombres"] = hombres
residentes["Mujeres"] = mujeres
residentes["Kids"] = niños

for key,valor in residentes.items():
    if key == "Mujeres":
        sumaHab = valor + residentes["Kids"]
    
print(f"Cantidad de habitantes entre mujeres y niños: {sumaHab}")