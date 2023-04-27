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
            sentencia = "UPDATE persona SET nombre = %s, apellido =%s,email=%s WHERE id_persona = %s"
            valores = (
                ("Kina", "YT", "Kinkinyt@gmail.com", 57),
                ("Beibi", "Juva", "Pein@gmail.com", 56)
            )
            # Tambien se usa executemany
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f"Registros actualizados: {registros_actualizados}")

except Exception as e:
    print(f"Error: {e}")

finally:
    conexion.close()
    print("Se cerró la conexion")
