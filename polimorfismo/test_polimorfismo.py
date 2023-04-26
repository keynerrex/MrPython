from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())

    # Preguntar si cierto metodo es de cierta clase
    # Con el metodo isinstance()
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Keyner", 1000000)
imprimir_detalles(empleado)


gerente = Gerente("Santiago", 4300000, "Backend")
imprimir_detalles(gerente)


# Metodo isinstance()   
    