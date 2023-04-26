from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)
        self._marca = marca
        self._tipoentrada = tipo_entrada

    def __str__(self) -> str:
        return f"Id: {self._id_teclado} Marca: {self._marca}, Tipo: {self._tipo_entrada}"


# if __name__ == "__main__":
#     teclado1 = Teclado("Asus", "USB")
#     print(teclado1)
