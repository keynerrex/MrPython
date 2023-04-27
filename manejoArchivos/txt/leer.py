archivo = open("keyner.txt", "r", encoding="utf8")

# Leer algunos caracteres (5) caracteres
# print(archivo.read(5))


# Leer lineas completas
# Pero solo por linea
# print(archivo.readline())

# Otras formas
# Leer todas las lineas
# for linea in archivo:
#     print(linea)

# Leer todas las lineas
# print(archivo.readlines())

# Acceder a sola una linea
# print(archivo.readlines()[0])

# Abrimos nuevo archivo
archivo2 = open("copia.txt", "a", encoding="utf8")
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print("Copiado...")