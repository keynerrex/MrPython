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

            sentencia = "DELETE FROM persona WHERE id_persona IN %s"
            entrada = input("Id a eliminar(Separados por coma):  ")
            # Si es una, poner coma
            # Split(para separar los caracteres)
            # Se convierte a tupla
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f"Registros eliminados: {registros_eliminados}")

except Exception as e:
    # Si algo falla se devuelven los cambios
    conexion.rollback()
    print(f"Error: {e}")

finally:
    conexion.close()
    print("Se cerró la conexion")
