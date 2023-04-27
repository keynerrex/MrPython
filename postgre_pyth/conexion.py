import psycopg2


class Conexion:

    conexion = psycopg2.connect(
        user="postgres",
        password="keynerdel2015",
        host="localhost",
        port="5432",
        database="test_db")



