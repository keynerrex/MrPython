from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("Creación de objeto Cuadrado".center(50, '-'))
cuadrado1 = Cuadrado(5, "Verde")
print(f"Calculo del area cuadrado: {cuadrado1.calcular_Area()}")
print(cuadrado1)

print("Creación de objeto Rectangulo".center(50, '-'))
rectangulo1 = Rectangulo(5, 6, "Azul")
print(f"Area del rectangulo: {rectangulo1.calcular_area()}")
print(rectangulo1)

# No se puede instaciar una clase abstracta
# figura = FiguraGeometrica()
