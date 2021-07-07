#Teoria Try Except

def spam(dividirPor):
    try:
        return 42 / dividirPor
    except:
        print('Se trato de dividir por cero')
    
num = int(input('Ingrese numero: '))

print(spam(num))