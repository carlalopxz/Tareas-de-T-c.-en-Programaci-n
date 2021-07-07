from os import error
import traceback

try:
    divisionPorCero = 2/ 0 
except:
    errorFile = open('Depuracion Codigo\\errorInfo.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('La informacion del Traceback fue guardada en errorInfo.txt')