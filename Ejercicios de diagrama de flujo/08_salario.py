#EJERCICIO 8

horasTrabajadas = 0
salarioPorHora = 0

print('Digite la cantidad de horas que trabaja y su salario por hora')
horasTrabajadas = int(input())
salarioPorHora = int(input())

salarioDiario = salarioPorHora * horasTrabajadas
salarioMensual = salarioDiario * 31

print('El salario mensual es de: ' + str(salarioMensual))