class Nombre:
    def __init__(self):
        self.nombre = None

    def definir_nombre(self, nombre):
        self.nombre = nombre
        print(self.nombre)


minombre = Nombre()
minombre.definir_nombre("Keyner")

