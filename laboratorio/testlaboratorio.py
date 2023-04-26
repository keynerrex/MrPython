from Orden import Orden
from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora


if __name__ == "__main__":
    teclado = Teclado("HP", "USB")
    raton = Raton("ROG", "USB")
    monitor = Monitor("DELL", "26cm")

    teclado2 = Teclado("Redmagic", "USB")
    raton2 = Raton("Asus", "USB")
    monitor2 = Monitor("Nitro", "34cm")

    computadora = Computadora("HP", monitor, teclado, raton)
    computadora2 = Computadora("Delirio", monitor2, teclado2, raton2)
  

computadoras = [computadora, computadora2]
orden1 = Orden(computadoras)
print(orden1)

print("Keyner Santiago Oliveros Florez")