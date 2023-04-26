class MiClase:
    variable_clase = "Valor variable clase"

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # metodo de clase -> palabra reservada cls de clase
    # cls es como self, acceder a metodos de clase

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)


MiClase.metodo_estatico()
