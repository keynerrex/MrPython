# Variable de clase
class MiClase:
    variable_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # No recibe self
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)
        pass


# print(MiClase.variable_clase)
# miClase = MiClase("Valor variable instancia")
# print(miClase.variable_instancia)
# print(miClase.variable_clase)


# miClase2 = MiClase("Otro valor de variable instancia")
# print(miClase2.variable_instancia)


# Clase al vuelo -> en cualquier momento

# miClase2.variable_clase2 = "Valor variable clase 2"
# print(miClase2.variable_clase2)


# Metodos de clase (Estaticos y metodos de clase)
MiClase.metodo_estatico()
