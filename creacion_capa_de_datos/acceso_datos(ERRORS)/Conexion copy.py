from prueba_logging import log
from psycopg2 import pool
import sys


class Conexion:

    _DATABASE = "test_db"
    _USERNAME = "postgres"
    _PASSWORD = "keynerdel2015"
    _DB_PORT = "5432"
    _HOST = "localhost"
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    # _conexion = None
    # _cursor = None

    # @classmethod
    # def obtener_conexion(cls):
    #     if cls._conexion is None:
    #         try:
    #             cls._conexion = db.connect(
    #                 host=cls._HOST, user=cls._USERNAME, password=cls._PASSWORD, port=cls._DB_PORT, database=cls._DATABASE)
    #             log.debug(f"Conexion exitosa a la base de datos: {cls._conexion}")
    #             return cls._conexion
    #         except Exception as e:
    #             log.debug(f"ocurrio un error al conectarse: {e}")
    #             sys.exit()
    #     else:
    #         return cls._conexion

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host = cls._HOST,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      port = cls._DB_PORT,
                                                      database = cls._DATABASE)
                log.debug(f"Creacion pool exitosa: {cls._pool}")
            except Exception as e:
                log.error(f"Error al obtener pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pool().getconn()
        log.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion

    # @classmethod

    def obtener_cursor(cls):
        pass
    #     if cls._cursor is None:
    #         try:
    #             cls._cursor = cls.obtener_conexion().cursor()
    #             log.debug(f"Se abrió el cursor: {cls._cursor}")
    #             return cls._cursor
    #         except Exception as e:
    #             log.error(f"Ocurrio una excepcion al ejecutar el cursor: {e}")
    #             sys.exit()
    #     else:
    #         return cls._cursor


# if __name__ == "__main__":
conexion1 = Conexion.obtener_conexion()
conexion2 = Conexion.obtener_conexion()
conexion3 = Conexion.obtener_conexion()
conexion4 = Conexion.obtener_conexion()
conexion5 = Conexion.obtener_conexion()
    # conexion6 = Conexion.obtener_conexion()
    # conexion7 = Conexion.obtener_conexion()
    # conexion8 = Conexion.obtener_conexion()
