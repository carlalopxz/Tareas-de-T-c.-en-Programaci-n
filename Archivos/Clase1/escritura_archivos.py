import os
direccion_de_trabajo = os.getcwd()
#print(direccion_de_trabajo) #D:\repositorios\tecnicas_en_programacion
#DIRECCION TEXTO: D:\repositorios\tecnicas_en_programacion\Archivos\Clase1\texto_ejemplo.txt
openFile = open(r'Archivos\Clase1\texto_ejemplo.txt','w')
openFile.write('''Este es un texto ejemplo
Para practicar el write del tema de Archivos
Fin. ''')
openFile.close()
openFile = open(r'Archivos\Clase1\texto_ejemplo.txt','a')
sobreEscritura_archivo = openFile.write('''\nEste es un texto para practicar
la sobreescritra en los Archivos.
Fin.''')
openFile.close()