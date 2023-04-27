class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print("Recurso obtenido".center(50, "-"))
        self.nombre = open(self.nombre, "r", encoding="utf8")
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print("Recurso cerrado".center(50, "-"))
        if self.nombre:
            self.nombre.close()
