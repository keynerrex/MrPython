from UsuarioDao import UsuarioDao
from logger_base import log
from Usuario import Usuario
opcion = None

while opcion != 5:
    print("""Opciones: 
          1. Listar usuarios
          2. Agregar Usuario
          3. Modificar usuario
          4. Eliminar usuario
          5. Salir
          """)
    opcion = int(input("Escribe tu opcion(1-5): "))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion == 2:
        username_var = input("Escriba el usuario: ")
        password_var = input("Escriba la contraseña: ")
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f"Usuarios insertados: {usuarios_insertados}")
    elif opcion == 3:
        id_usuario_var = int(input("Escribe el id del usuario a modificar: "))
        username_var = input("Escribe el nuevo usuario: ")
        password_var = input("Escribe la nueva contraseña: ")
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        log.info(f"Usuarios actualizados: {usuarios_actualizados}")
    elif opcion == 4:
        id_usuario_var = int(input("Escribe el id del usuario a eliminar: "))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f"Usuarios eliminados: {usuarios_eliminados}")

    else:
        log.info("Salimos de la aplicacion")
