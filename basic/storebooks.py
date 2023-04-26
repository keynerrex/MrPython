"""
# Nombre del libro
# Id del libro
# Precio del libro
# Envio
"""

nombre_libro = input("Proporcione el nombre del libro: ")
id_libro = int(input("Proporcione el id del libro: "))
precio_libro = float(input("Proporcione el precio del libro: "))
paga_envio = (input("El envío es gratis?: "))

env = {
    "si": "SI",
    "no": "NO",
}
while paga_envio not in env:
    paga_envio = (input("Escriba una respuesta corecta: "))


def guardar_libro(id, nombre, precio, envio):
    libro = {"id": id, "nombre": nombre, "precio": precio, "envio": envio}
    libros.append(libro)
    return print("Libro Guardado exítosamente")


def consultar_libro(id, nombre, precio, envio):
    print(f"""
    Resultados de su busquedad
    Id del libro: {id}
    Nombre del libro: {nombre}
    Precio del libro: {precio}
    Incluye envio Gratis?: {envio}
""")


libros = []

guardar_libro(id_libro, nombre_libro, precio_libro, paga_envio)
consultar_libro(id_libro, nombre_libro, precio_libro, paga_envio)
