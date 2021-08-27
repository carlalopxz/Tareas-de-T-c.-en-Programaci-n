openFile = open(r'Archivos\Clase1\texto_ejemplo.txt','r')
#readFile = openFile.read()
metodo_readlines = openFile.readlines()
openFile.close()
#print(readFile)
for lineas in metodo_readlines:
    print(lineas)
