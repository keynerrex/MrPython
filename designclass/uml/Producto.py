class Producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    def __str__(self) -> str:
        return f"\n[Id producto: {self._id_producto}] [Nombre: {self._nombre}] [Precio: ${self._precio}]"

    @property
    def precio(self):
        return self._precio
