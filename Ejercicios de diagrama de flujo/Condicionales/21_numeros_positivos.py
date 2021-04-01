print('Digite dos numeros')
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('Los dos numeros son positivos: ' + str(x) + ' ,' + str(y))
elif x < 0 and y < 0:
    print('Los dos numeros son menores a cero')
elif x > 0:
    print('Solo el numero ' + str(x) + ' es mayor a cero')
else:
    print('Solo el numero ' + str(y) + ' es mayor a cero')
    