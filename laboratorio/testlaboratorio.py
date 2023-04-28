from Orden import Orden
from Teclado import Teclado
from Raton import Raton
from Monitor import Monitor
from Computadora import Computadora


if __name__ == "__main__":

    compTeclado = str(input("Escriba la marca del teclado: "))
    compTeclado_entrada = str(input("Escriba el tipo de entrada: "))

    compRaton = str(input("Escriba la marca del mouse: "))
    compRaton_entrada = str(input("Escriba el tipo de entrada: "))
    
    compMonitor = str(input("Escriba la marca del monitor: "))
    compMonitor_tamaño = str(input("Escriba el tamaño del monitor: "))
    
    teclado = Teclado(compTeclado, compTeclado_entrada)
    raton = Raton(compRaton, compRaton_entrada)
    monitor = Monitor(compMonitor,compMonitor_tamaño )

    # teclado2 = Teclado("Redmagic", "USB")
    # raton2 = Raton("Asus", "USB")
    # monitor2 = Monitor("Nitro", "34cm")
    marca_computadora = str(input("Marca del computador: "))
    
    computadora = Computadora(marca_computadora, monitor, teclado, raton)
    # computadora2 = Computadora("Delirio", monitor2, teclado2, raton2)


computadoras = [computadora]
orden1 = Orden(computadoras)
print(orden1)

print("Keyner Santiago Oliveros Florez")
