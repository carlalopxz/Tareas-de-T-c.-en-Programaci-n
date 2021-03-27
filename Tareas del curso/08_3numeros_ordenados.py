#Pedir tres números y mostrarlos ordenados de mayor a menor.

print('Digite 3 números')
x = int(input())
y = int(input())
z = int(input())

if x > y and x > z and y > z:
    print(str(x) + ' > ' + str(y) + ' > ' + str(z))
elif x > y and x > z and z > y:
    print(str(x) + ' > ' + str(z) + ' > ' + str(y))
elif y > x and y > z and x > z:
    print(str(y) + ' > ' + str(x) + ' > ' + str(z))
elif y > x and y > z and z > x:
    print(str(y) + ' > ' + str(z) + ' > ' + str(x))
elif z > x and z > y and y > x:
    print(str(z) + ' > ' + str(y) + ' > ' + str(x))
elif z > x and z > y and x > y:
    print(str(z) + ' > ' + str(x) + ' > ' + str(y))
elif x == y and x == z:
    print('Los 3 números son iguales')

#OPCION 2

if x > y and x > z:
    if y > z:
        print(str(x) + ' > ' + str(y) + ' > ' + str(z))
    else:
        print(str(x) + ' > ' + str(z) + ' > ' + str(y))
if y > x and y > z:
    if x > z:
        print(str(y) + ' > ' + str(x) + ' > ' + str(z))
    else:
        print(str(y) + ' > ' + str(z) + ' > ' + str(x))
if z > x and z > y:
    if x > y:
        print(str(z) + ' > ' + str(x) + ' > ' + str(y))
    else:
        print(str(z) + ' > ' + str(y) + ' > ' + str(x))
if x == y and x == z:
    print('Los 3 números son iguales')
