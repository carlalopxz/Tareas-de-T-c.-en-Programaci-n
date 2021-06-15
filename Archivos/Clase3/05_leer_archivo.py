#Escribe un programa que pueda abrir un archivo y:
#a) Contar la cantidad de palabras.
#b) Encontrar la palabra más larga.
#c) Contar la frecuencia de cada palabra.

import os,pprint

nameFile = r'Archivos\Clase3\texto_ejemplo.txt'
if os.path.exists(nameFile):
    print('Open File')
    openFile = open(nameFile)
else:
    print('File not Found')

readFile = openFile.read()
openFile.close()
word = readFile.split()

while True:
    opcion = input('''Eliga una opcion: 
A) Contar palabras
B) Buscar palabra mas larga
C) Contar la frecuencia de las palabras
D) Salir del programa
''').lower()
    def contar_palabras():
        acum = 0
        for palabras in range(len(word)):
            acum += palabras
        print(f'Cantidad de caracteres: {acum}')

    def word_long():
        pass
        caracteres_palabra_larga = 0
        palabra_mas_larga = ''
        for palabra in word:
            if len(palabra) >= caracteres_palabra_larga:
                palabra_mas_larga = palabra
                caracteres_palabra_larga = len(palabra)
        print(f'La palabra más larga es {palabra_mas_larga} con {caracteres_palabra_larga} caracteres de largo.')

    def frecuencia_palabras():
        dicc_palabras = {}
        for palabras in word:
            dicc_palabras[palabras] = word.count(palabras)
        pprint.pprint(dicc_palabras)

    if opcion == 'a':
        contar_palabras()
    if opcion == 'b':
        word_long()
    if opcion == 'c':
        frecuencia_palabras()
    if opcion == 'd':
        print('Saliò existosamente del programa')
        break  
    print('Close File')