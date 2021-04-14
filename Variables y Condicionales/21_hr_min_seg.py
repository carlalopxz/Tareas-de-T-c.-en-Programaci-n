#Pedir una hora de la forma hora, minutos y segundos, y mostrar la hora en el segundo siguiente.

hr = int(input('Digite la hora \n'))
minutos = int(input('Digite los minutos \n'))
seg = int(input('Digite los segundos \n'))

seg = seg + 1

if minutos > 59:
    minutos = 0 
if hr > 23:
    hr = 0
if seg > 59:
    seg = 0
    minutos = minutos + 1
    if minutos > 59:
        minutos = 0
        hr = hr + 1
        if hr > 23:
            hr = 0

print(f'La hora es {hr}:{minutos}:{seg}')
    