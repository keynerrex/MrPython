from Vehiculo import *

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+f"Velocidad: {self.velocidad}"


carro = Coche("Blanco",4,"200Km")
print(carro)