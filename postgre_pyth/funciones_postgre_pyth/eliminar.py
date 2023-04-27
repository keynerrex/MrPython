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

            sentencia = "DELETE FROM persona WHERE id_persona = %s"
            # Si es una, poner coma
            valores = (57,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f"Registros eliminados: {registros_eliminados}")

except Exception as e:
    print(f"Error: {e}")

finally:
    conexion.close()
    print("Se cerró la conexion")
