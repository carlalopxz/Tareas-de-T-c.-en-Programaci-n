#Pedir dos números y decir si uno es múltiplo del otro.

x = 0
y = 0 

print('Digite dos números')
x = int(input())
y = int(input())

if x % y == 0:
    print('El numero ' + str(x) + ' es multiplo de ' + str(y))
else:
    print('El numero ' + str(x) + ' no es multiplo de ' + str(y))