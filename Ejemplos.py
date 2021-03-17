#Acá voy a poner ejemplos que encuentre

#Ejemplo del diagrama de flujo 

totalAlumnos = input('Ingrese el número total de alumnos')
numeroDeMujeres = input('Ingrese el número de mujeres que hay en el salon')

def porcentajeAlumnas(totalAlumnos, numeroDeMujeres):
    resultado1 = int((numeroDeMujeres*100)/totalAlumnos)
    return resultado1
    print(resultado1)

porcentajeAlumnas(totalAlumnos, numeroDeMujeres)

#Funciones

def mensaje():
    print('Estamos aprendiendo funciones')

mensaje()

def suma1():
    num1 = 5
    num2 = 7
    print(num1+num2)

suma1()

def suma2(num1, num2):
    print(num1 + num2)

suma2(3,4)
suma2(5,8)

def suma3(num3,num4):
    resultado = num3 + num4
    return resultado

print(suma3(3,4))
print(suma3(5,8))

almacena_resultado = suma3(6,5)

print(almacena_resultado)