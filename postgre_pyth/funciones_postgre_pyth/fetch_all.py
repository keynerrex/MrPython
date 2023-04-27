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
            sentencia = "SELECT * FROM persona WHERE id_persona IN %s"
            # Meter la tupla en un atupla
            # y la coma para que sepa que es una sola
            # llaves_primarias = ((43, 53, 54),)

            entrada_id = input(
                'Proporciona los id\'s a buscar(separado por comas): ')
            # Va quitar las comas para que solo de los numeros split()
            # Lo pasamos a una tupla -> se mete tupla en tupla
            llaves_primarias = (tuple(entrada_id.split(',')),)
            cursor.execute(sentencia, llaves_primarias)
            # Acá se usa el metotodo fectall()
            # Trae todos los datos
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

except Exception as e:
    print(f"Error: {e}")

finally:
    conexion.close()
    print("Se cerró la conexion")
