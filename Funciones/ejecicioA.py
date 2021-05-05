#Crear una funcion “Login”, que recibe un nombre de usuario y una contraseña y
#te devuelve True si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 

#Además esta funcion recibe el número de intentos que se ha intentado hacer login y 
#si no se ha podido hacer login incremente este valor.

#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
#solamente tenemos tres oportunidades para intentarlo.

def login(user,password):
    
    if user == 'usuario1' and password == 'asdasd':
        True

usuario = input('Ingrese su nombre de usuario \n')
contrasenia = input('Ingrese su contraseña \n')

if login(usuario,contrasenia):
    print('Usuario y contraseña corecctos')
else:
    print('Usuario y contraseña incorrectos')
