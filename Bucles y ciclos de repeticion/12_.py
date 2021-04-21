#Pedir un número y calcular su factorial. 

#Ejemplos:
#factorial de 7 = 7 * 6 * 5 * 4 * 3 * 2 * 1
#factorial de 7 = 1 * 2 * 3 * 4 * 5 * 6 * 7 
#factorial de 5 = 1 * 2 * 3 * 4 * 5
#factorial de 5 = 5 * 4 * 3 * 2 * 1

i = int(input('Digite un número \n'))
mult = 1

for i in range(1,i+1,1):
    mult = mult * i
    print(mult)  