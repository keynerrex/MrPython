from logger_base import log
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

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f"Creacion pool exitosa: {cls._pool}")
            except Exception as e:
                log.error(f"Error al obtener pool: {e}")
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtener_conexion(cls):
        if cls._pool is None:
            cls.obtener_pool()
        conexion = cls._pool.getconn()
        log.debug(f"Conexión obtenida del pool: {conexion}")
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pool().putconn(conexion)
        log.debug(f"Regresamos la conexion al pool: {conexion}")

    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pool().closeall()


if __name__ == "__main__":
    conexion1 = Conexion.obtener_conexion()
    conexion1.liberar_conexion(conexion1)

    conexion2 = Conexion.obtener_conexion()
