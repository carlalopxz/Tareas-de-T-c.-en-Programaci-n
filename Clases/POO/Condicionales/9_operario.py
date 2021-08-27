# Se tiene registrado la producción (unidades) logradas por un operario a lo largo de la semana (lun a sab)
# Elabore un algoritmo que nos muestre o nos diga si el operario recibirá incentivos sabiendo que el promedio
# de producción minima es de 100 unidades. 

produccion = int(input("Ingrese la produccion que tuvo a lo largo de la semana:\n"))

if produccion >= 100:
    print("Felicidades! Llegó a la minina de produccion semanal, recibira un incentivo!")
else:
    print("No llego a la produccion minima semanal.")