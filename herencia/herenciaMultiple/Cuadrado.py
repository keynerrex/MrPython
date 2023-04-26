from FiguraGeometrica import FiguraGeometrica
from Color import Color
# from Color import Color as color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__(lado)
        # Todos los lados iguales

        # Herencia multiple
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcularArea(self):
        return self.alto * self.ancho
