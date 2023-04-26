# class Persona:
#     def __init__(self):
#         self.edad = "Keyner"
#         self.apellido = "Oliveros"
#         self.edad = 19


# persona1 = Persona()
# print(persona1.nombre)


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrardates(self):
        print(f"{self.nombre}, {self.apellido}, {self.edad}")


persona1 = Persona("Keyner", "Oliveros", 19)
persona1.mostrardates()
