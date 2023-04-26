"""
# Nombre del libro
# Id del libro
# Precio del libro
# Envio
"""
#Forma mejorada

def guardar_libro(libros, id, nombre, precio, envio):
    libro = {"id": id, "nombre": nombre, "precio": precio, "envio": envio}
    libros.append(libro)
    print("Libro guardado exitosamente")


def consultar_libro(libros, id):
    for libro in libros:
        if libro["id"] == id:
            print(f"""
                Resultados de su búsqueda
                Id del libro: {libro["id"]}
                Nombre del libro: {libro["nombre"]}
                Precio del libro: {libro["precio"]}
                Incluye envío gratis?: {libro["envio"]}
            """)
            return
    print("No se encontró ningún libro con ese ID")


libros = []

nombre_libro = input("Proporcione el nombre del libro: ")
id_libro = None
while not id_libro:
    try:
        id_libro = int(input("Proporcione el id del libro: "))
    except ValueError:
        print("El ID del libro debe ser un número entero")

precio_libro = None
while precio_libro is None:
    try:
        precio_libro = float(input("Proporcione el precio del libro: "))
    except ValueError:
        print("El precio del libro debe ser un número decimal")

paga_envio = input("El envío es gratis? (si/no)").lower()
while paga_envio not in ["si", "no"]:
    paga_envio = input("Escriba una respuesta correcta (si/no)").lower()

guardar_libro(libros, id_libro, nombre_libro, precio_libro, paga_envio)
consultar_libro(libros, id_libro)
