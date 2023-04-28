from conexion import Conexion

# Conexion a la clase conexion
conexion = Conexion.conexion
cursor = conexion.cursor()

# Validaciones no pueden ir vacios
nombre_persona = str(input("Nombre: "))
while not nombre_persona.isalpha():
    nombre_persona = str(input("Ingrese un nombre valído:"))

apellido_persona = input("Apellido: ")
while not apellido_persona.isalpha():
    apellido_persona = str(input("Ingrese un apellido valído: "))

correo = input("Correo: ")
while '@' not in correo:
    correo = str(input("Ingrese un correo valído(ej: keyner@gmail.com):"))

# Inserccion de datos tabla persona
try:
    query = "INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)"
    values = (nombre_persona, apellido_persona, correo)
    cursor.execute(query, values)
    conexion.commit()

except Exception as e:
    print(f"Error inserting:{e}")
print("Insercción correcta")


# Preguntar si quiere ver los datos tabla persona
ver = str(input("Quiere ver los datos?: "))
try:
    query = "SELECT * FROM persona ORDER BY id_persona"
    cursor.execute(query)
    registros = cursor.fetchall()
    if ver == "si":
        for datos in registros:
            print(datos)
    else:
        print("De acuerdo, no se mostrarán los datos")
except Exception as e:
    print(f"Error al traer: {e}")
# Cerrar la conexion
finally:
    conexion.close()
    print("Conexion cerrada")
