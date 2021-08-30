# Tenemos la siguiente lista de animales = ["Oso hormiguero","Tejon","Pato","Emu","Zorro del desierto"]
# Debemos obtener el index de "Pato" para luego insertar en su lugar "Cobra"

animales = ["Oso hormiguero","Tejon","Pato","Emu","Zorro del desierto"]

index = animales.index("Pato")

animales.insert(index,"Cobra")

print(animales)