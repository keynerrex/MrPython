from Vehiculo import *


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+f"Tipo: {self.tipo}"


bicicleta = Bicicleta("Rojo", 2, "Ruta")
print(bicicleta)
