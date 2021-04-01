print('Digite 3 numeros')
x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    print('El numero ' + str(x) + ' es el mayor')
elif y > z:
    print('El numero ' + str(y) + ' es el mayor')
else:
    print('El numero ' + str(z) + ' es el mayor')