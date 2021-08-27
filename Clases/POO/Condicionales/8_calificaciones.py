# Capturar las calificaciones obtenidas por un estudiante en tres examenes parciales e imprimir su promedio final
# Seguido del mensaje correspondiente de acuerdo a la siguiente tabla.
#|_Promedio___|__Mensaje___|
#|   100      | Excelente  |
#|90 y < 100  | Muy bien   |
#|80 y < 90   | Bien       |
#|70 y < 80   | Regular    |
#|60 y < 70   | Suficiente |
#|59 o -      | Reprobado  |

parcial1 =  int(input("Ingrese la nota del parcial 1:\n"))
parcial2 = int(input("Ingrese la nota del parcial 2:\n"))
parcial3 = int(input("Ingrese la nota del parcial 3:\n"))

notaF = parcial1 + parcial2 + parcial3
promedioF = notaF / 3

if promedioF == 100:
    print(f"Promedio: {promedioF} - ¡Excelente!")
elif promedioF >= 90 and promedioF < 100:
    print(f"Promedio: {promedioF} - ¡Muy bien!")
elif promedioF >= 80 and promedioF < 90:
    print(f"Promedio: {promedioF} - ¡Bien!")
elif promedioF >= 70 and promedioF < 80:
    print(f"Promedio: {promedioF} - Regular.")
elif promedioF >= 60 and promedioF < 70:
    print(f'Promedio: {promedioF} - Suficiente.')
elif promedioF <= 59:
    print(f"Promedio: {promedioF} - Reprobado.")