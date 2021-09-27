# Tenemos el siguiente puntaje score = {"a" = 1, "c" = 3,"b"=3,"e"= 1,"d"=2,"g"=2,"f"=4,"i"=1,"h"=4,"k"=5,"j"=8,"m"=3,"l"=1,"o"=1,"n"=1,"q"=10,"p"=3,"s"=1,"r"=1,"u"=1,"t"=1,"w"=4,"v"=4,"y"=4,"x"=8,"z"=10}
# Tenmos que realizar una funcion que al poner una palabra nos diga cual es su puntaje
# Ojo con poner mayusculas y minusculas, la funcion debe tomarlas igual

score = {"a": 1, 
         "c": 3,
         "b": 3,
         "e": 1,
         "d": 2,
         "g": 2,
         "f": 4,
         "i": 1,
         "h": 4,
         "k": 5,
         "j": 8,
         "m": 3,
         "l": 1,
         "o": 1,
         "n": 1,
         "q": 10,
         "p": 3,
         "s": 1,
         "r": 1,
         "u": 1,
         "t": 1,
         "w": 4,
         "v": 4,
         "y": 4,
         "x": 8,
         "z": 10}

tupla = input("Ingrese la palabra a calcular el puntaje:\n").lower()

def puntos(tupla):
    sumaPuntos = 0
    for i in tupla:
        for j in score.keys():
            if i == j:
                sumaPuntos += score[j]

    print(f"El puntaje de la palabra '{tupla}': {sumaPuntos}")

puntos(tupla)