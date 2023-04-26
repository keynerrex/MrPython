from Producto import Producto
from Orden import Orden

producto1 = Producto("Abrigo", 100.000)
producto2 = Producto("Zapatos", 343.445)
producto3 = Producto("Medias", 5.400)
producto4 = Producto("Gorra", 9.500)

total_productos1 = [producto1, producto2]

total_productos2 = [producto3, producto4]

orden1 = Orden(total_productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(orden1.calcular_total())

orden2 = Orden(total_productos2)
print(orden2)
print(orden2.calcular_total())

# Sobrecarga de operadores
