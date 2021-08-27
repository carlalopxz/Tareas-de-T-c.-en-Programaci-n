# A un trabajador le descuentan de su sueldo el 10% si su sueldo es menor o igual a 1000.
# Por encima de 1000 y hasta 2000 el 5% del adicional.
# Por encima de 2000 el 3% adicional.
# Calcular el descuento y sueldo neto que recibe el trabajador dado su sueldo. 

sueldo = int(input("Ingrese su sueldo:\n"))

if sueldo <= 1000:
    descuento = (sueldo * 10) / 100
    sueldoNeto = sueldo - descuento
    porcentaje = 10
elif sueldo > 1000 and sueldo <= 2000:
    descuento = (sueldo * 5) / 100
    sueldoNeto = sueldo - descuento
    porcentaje = 5
elif sueldo > 2000:
    descuento = (sueldo * 3) / 100
    sueldoNeto = sueldo - descuento
    porcentaje = 3

print(f"Su sueldo NETO es de: ${sueldoNeto} con el descuento del {porcentaje}% (${descuento})")