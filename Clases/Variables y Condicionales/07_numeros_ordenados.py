#Pedir dos números y mostrarlos ordenados de mayor a menor.

print('Digite dos números')
num1 = input()
num2 = input()

if int(num1) > int(num2):
    print('El numero ' + num1 + ' es mayor que ' + num2)
elif int(num1) < int(num2):
    print('El numero ' + num2 + ' es mayor que ' + num1)