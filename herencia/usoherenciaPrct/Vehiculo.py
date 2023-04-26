class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f"""
        Color: {self.color}
        Ruedas: {self.ruedas}
        """
