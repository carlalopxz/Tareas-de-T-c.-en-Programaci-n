#Pedir dos números y mostrarlos ordenados de mayor a menor.

print('Digite dos números')
num1 = input()
num2 = input()

if int(num1) > int(num2):
    print('El numero ' + num1 + ' es mayor que ' + num2)
elif int(num1) < int(num2):
    print('El numero ' + num2 + ' es mayor que ' + num1)

#Resuelve: Valeria Acosta

print('Ingrese dos numeros')
numero1=int(input())
numero2=int(input())

if numero1 > numero2:
    print ('Es mayor'+ str(numero1)+' y es menor'+str(numero2))
else:
    print('Es menor'+ str(numero1)+'y es mayor el'+ str(numero2))

#Resuelve: Exequiel Ibarra

print ('ingrese dos numeros')
n1 = input()
n2 = input()
if int (n1) > int (n2):
    print ('el orden es '+n1 +', '+ n2)
elif int (n1) < int(n2):
    print ('el orden es '+n2 +', ' + n1)


#Resuelve: Miguel Rotela
print('ingrese 2 numeros')
num1=int(input())
num2=int(input())
if num1>num2:
    print(num1, num2)
elif num2>num1:
    print(num2, num1)
else:
    print('Los numeros son iguales')