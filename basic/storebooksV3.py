"""
# Nombre del libro
# Id del libro
# Precio del libro
# Envio
"""

# Tercera version simplificada

libros = []

nombre_libro = input("Proporcione el nombre del libro: ")
id_libro = int(input("Proporcione el id del libro: "))
precio_libro = float(input("Proporcione el precio del libro: "))
paga_envio = input("El envío es gratis? (si/no)").lower()

while paga_envio not in ["si", "no"]:
    paga_envio = input(
        "Escriba si o no para indicar si el envío es gratis: ").lower()

libros.append({"id": id_libro, "nombre": nombre_libro,
              "precio": precio_libro, "envio": paga_envio})

print("Libro guardado exitosamente")

id_consulta = int(input("Ingrese el ID del libro que desea buscar: "))
encontrado = False

for libro in libros:
    if libro["id"] == id_consulta:
        encontrado = True
        print(f"""
            Resultados de su búsqueda
            ---------------
            Id del libro: {libro["id"]}
            Nombre del libro: {libro["nombre"]}
            Precio del libro: {libro["precio"]}
            Incluye envío gratis?: {libro["envio"]}
        """)

if not encontrado:
    print("No se encontró ningún libro con ese ID")
