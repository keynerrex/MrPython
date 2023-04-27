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
            sentencia = "SELECT id_persona, nombre FROM persona WHERE id_persona = %s"
            id_persona = 43
            # Para que sepa si es una tupla, ponerle una coma
            cursor.execute(sentencia, (id_persona,))
            # Acá se usa el metotodo fectone()
            # Trae un registro
            registros = cursor.fetchone()
            print(registros)

except Exception as e:
    print(f"Error: {e}")

finally:
    conexion.close()
    print("Se cerró la conexion")
