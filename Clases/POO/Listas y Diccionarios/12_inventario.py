# Realizar un inventario de los siguientes productos:
# Harina: 500 unidades
# Aceite: 800 unidades
# Arroz: 400 unidades
# Leche: 900 unidades
# Agua: 2000 unidades
# Luego borrar 1000 unidades de agua y 200 de aceite
# Agregar 1500 de agua y 200 de leche
# Borrar por ultimo las 500 unidades de harina

inventario = {}
inventarioUpdate = {}
while True:
    opcion = input("A) Agregar al inventario\nB) Eliminar del inventario unidades\nC) Update Inventario\nD) Eliminar\n0 para terminar\n").lower()
    if opcion == "a":
        while opcion == "a":
            key  = input("Producto para agregar:\n").lower()
            valor = input("Cantidad de unidades: \n").lower()
            inventario[key] = valor
            opcion = input("A) Seguir\nO para terminar\n").lower()
            if opcion == "0":
                break
        for k,v in inventario.items():
            print(f"{k}: {v}")
    if opcion == "b":
        while opcion == "b":
            keyUpdate = input("Ingrese el producto para eliminar unidades:\n").lower()
            valorUpdate = input("Ingrese las unidades a eliminar:\n").lower()
            inventarioUpdate[keyUpdate] = valorUpdate
            inventario.update(inventarioUpdate)
            opcion = input("A) Seguir eliminando\n0 para terminar\n").lower()
            if opcion == "0":
                break
        for k,v in inventario.items():
            print(f"{k}: {v}")
    if opcion == "c":
        while opcion == "c":
            keyUpdate = input("Ingrese el producto para agregarle unidades:\n").lower()
            valorUpdate = input("Ingrese las unidades a agregar:\n").lower()
            inventarioUpdate[keyUpdate] = valorUpdate
            inventario.update(inventarioUpdate)
            opcion = input("A) Seguir agregando\n0 para terminar\n").lower()
            if opcion == "0":
                break
        for k,v in inventario.items():
            print(f"{k}: {v}")
    if opcion == "d":
        while opcion == "d":
            keyEliminar = input("Ingrese el producto a eliminar:\n").lower()
            del inventario[keyEliminar]
            opcion = input("A) Seguir\nO para terminar")
        if opcion == "0":
            break
        for k,v in inventario.items():
            print(f"{k}: {v}")
    if opcion == "0":
        break