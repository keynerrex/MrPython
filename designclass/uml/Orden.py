from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return f"Total: ${total} Pesos"

    def __str__(self) -> str:
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__()
        return f"[Orden: {self._id_orden}] \nProductos: {productos_str}"
