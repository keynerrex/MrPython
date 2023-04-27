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
            sentencia = "INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)"
            valores = (
                ("Carlos", "Lara", "carlos@gmail.com"),
                ("Juan", "Alto", "juaAlfds@gmail.com")

            )
            # Se cambia el metodo a executemany
            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f"Registros insertados: {registros_insertados}")

except Exception as e:
    print(f"Error: {e}")

finally:
    conexion.close()
    print("Se cerró la conexion")
