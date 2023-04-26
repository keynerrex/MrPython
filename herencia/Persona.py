class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre} edad: {self.edad}"


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    # acceder a la función de la class Persona para reutilizar codigo
    def __str__(self):
        return super().__str__() + f" Sueldo: {self.sueldo}"
