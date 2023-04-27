import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="keynerdel2015",
    host="localhost",
    port="5432",
    database="test_db")

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM persona"
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)

except Exception as e:
    print(f"Error: {e}")

finally:
    conexion.close()
    print("Se cerró la conexion")
