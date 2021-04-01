print('Ingrese la cantidad de horas trabajadas')
horasTrab = int(input())

if horasTrab <= 40:
    salarioDia = horasTrab * 16
    salarioSemanal = salarioDia * 5
    print('Su salario semanal es de: $' + str(salarioSemanal))
else:
    salario1 = 40 * 16
    salario2 = (horasTrab - 40) * 20
    salarioDia = salario1 + salario2
    salarioSemanal = salarioDia * 5
    print('Su salario semanal es de: $' + str(salarioSemanal))
