
# ABC = Abstract Base Class
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if 0 < ancho < 10:
            self.ancho = ancho
        else:
            self.ancho = 0

        if 0 < alto < 10:
            self.alto = alto
        else:
            self.alto = 0

    @property
    def get_ancho(self):
        return f"Ancho: {self._ancho}"

    @get_ancho.setter
    def set_ancho(self, ancho):
        self._ancho = ancho

    @property
    def get_alto(self):
        return f"Alto: {self._alto}"

    @get_alto.setter
    def set_alto(self, alto):
        self._alto = alto

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self) -> str:
        return f"Figura Geometrica [Ancho: {self.ancho}, Alto: {self.alto}]"
