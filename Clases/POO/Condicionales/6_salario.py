# A un trabajador le pagan según sus horas y una tarifa de pago por horas.
# Si la cantidad de horas trabajadas es mayor a 40 horas, la tarifa se incrementa un 50% para las horas extras.
# Calcular el salario del trabajador dadas las horas trabajadas y la tarifa.

horasTrabajadas = int(input("Ingrese la cantidad de horas trabajas:\n"))
salarioXHora = int(input("Ingrese el salario por hora:\n"))
if horasTrabajadas > 40:
    tarifaHorasExtras = (50 * salarioXHora) / 100
    tarifaTotal = horasTrabajadas * (salarioXHora + tarifaHorasExtras)
else:
    tarifaTotal = horasTrabajadas * salarioXHora

print(f"Las horas trabajadas son: {horasTrabajadas}\nEl salario total es de: ${tarifaTotal}")