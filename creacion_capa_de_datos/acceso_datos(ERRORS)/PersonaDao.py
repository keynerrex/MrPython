from Conexion import Conexion
from Persona import Persona
from prueba_logging import log


class PersonaDao:

    # Data Access Object -> DAO ->tIENE EL CRUD

    """
    DAO (Data Access Object)
    CRUD(Create-Read-Update-Delete)
    """
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id_persona"
    _INSERTAR = "INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id_persona=%s"

    @classmethod
    def seleccionar(cls):
        with Conexion.obtener_cursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()

            # Agregarlos a una lista
            personas = []
            for registro in registros:
                # Podemos obtener con las posiciones
                persona = Persona(registro[0], registro[1],
                                  registro[2], registro[3])
                personas.append(persona)

                # Devuelve las listas de personas
            return personas

    @classmethod
    def insertar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.correo)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Persona Añadida: {persona}")
                return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.nombre, persona.apellido,
                           persona.correo, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f"Persona Actualizada: {persona}")
                return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtener_conexion():
            with Conexion.obtener_cursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f"Persona eliminada: {persona}")
                return cursor.rowcount


if __name__ == "__main__":
    # Insertar
    # persona1 = Persona(nombre="Keyner", apellido="Oliveros",
    #                    email="keynerkina@gmail.com")
    # personas_insertadas = PersonaDao.insertar(persona1)
    # log.debug(f"Personas insertadas: {personas_insertadas}")
    ########################
    # Select
    # personas = PersonaDao.seleccionar()
    # for persona in personas:
    #     log.debug(persona)
    ########################
    # Actualizar
    # persona = Persona(66, "Pelo", "pele", "jh@.com")
    # personas_actualizadas = PersonaDao.actualizar(persona)
    # log.debug(f"Personas actualizadas: {personas_actualizadas}")
    ##########################
    # Eliminar
    # persona = Persona(id_persona=66)
    # personas_eliminadas = PersonaDao.eliminar(persona)
    # log.debug(f"Personas eliminadas: {persona}")
    pass
