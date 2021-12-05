# from menu_inicial import MenuInicial
from baseDeDatos import baseDatos
from usuario import Usuario

# menuInicial = MenuInicial()

# resultadoMenu = menuInicial.menu()

cantidadDeUsuarios = len(baseDatos.selectTodoUsuario())

for x in range(cantidadDeUsuarios):
    globals() [f"usuario{x}"] = Usuario(*(baseDatos.selectTodoUsuario()[x]))

# print(globals()["usuario1"].get_nombre())
# print(globals()['usuario1'].get_id())
globals()['usuario14'].menuUsuarioInicial()
# print(globals()['usuario14'].get_email())
# print(globals()['usuario14'].get_nombre())
# print(globals()['usuario14'].get_apellido())
# print(globals()['usuario14'].get_email())
# print(globals()['usuario14'].get_password())
# print(globals()['usuario14'].get_celular())
# print(globals()['usuario14'].get_biografia())

# if len(list(resultadoMenu.keys())) > 2:
#     diccionarioMenu = dict(resultadoMenu)
#     usuario = Usuario(**diccionarioMenu)
# else:
#     print('Hola')
# print(usuario.get_nombre())
    