#REMOVER ESPACIOS EN BLANCO
print('METODO STRIP(), RSTRIP() Y LSTRIP()')
spam = ' Hola Mundo '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

print('--------------------------------------------------')

spam = 'SpamSpamCerdoSpamHuevosSpamSpam'
print(spam.strip('ampS'))