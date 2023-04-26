from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self) -> str:
        return f"""
        [{self._nombre}: {self._id_computadora}]
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        """


# if __name__ == "__main__":
#     teclado = Teclado("HP", "USB")
#     raton = Raton("ROG", "USB")
#     monitor = Monitor("DELL", "26cm")
#     computadora = Computadora("HP", monitor, teclado, raton)
#     computadora2 = Computadora("HP", monitor, teclado, raton)
#     print(computadora)
#     print(computadora2)