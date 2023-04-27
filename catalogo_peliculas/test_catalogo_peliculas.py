from dominio.Pelicula import Pelicula
from servicio.CatalogoPelicula import CatalogoPelicula as CatPeli
opcion = None
while opcion != 4:
    try:
        print("Opciones: ")
        print("1. Agregar pelicula")
        print("2. Ver peliculas")
        print("3. Eliminar pelicula")
        print("4. Salir")
        opcion = int(input("Escriba la opcion(1-4):"))

        if opcion == 1:
            nombre_pelicula = input("Nombre de la pelicula:")
            pelicula = Pelicula(nombre_pelicula)
            CatPeli.agregar_pelicula(pelicula)
        elif opcion == 2:
            CatPeli.listar_peliculas()

        elif opcion == 3:
            CatPeli.eliminar_pelicula()

    except Exception as e:
        print("Error: " + str(e))
else:
    print("---FIN---")
