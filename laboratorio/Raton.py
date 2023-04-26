from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):

        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    def __str__(self):
        return f"Id: {self._id_raton}, Marca: {self._marca}, Tipo de Entrada: {self._tipo_entrada}"


# if __name__ == "__main__":
#     raton1 = Raton("Asus", "USB")
#     print(raton1)
#     raton2 = Raton("Acer", "USB")
#     print(raton2)
