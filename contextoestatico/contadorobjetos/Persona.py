class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f"Persona [{self.id_persona} {self.nombre} {self.edad}]"


persona1 = Persona("Keyner", 19)
print(persona1)
persona2 = Persona("Santiago", 20)
print(persona2)
persona3 = Persona("Oliveros", 21)
print(persona3)
persona4 = Persona("Florez", 22)
print(persona4)

Persona.generar_siguiente_valor()
persona5 = Persona("Pedrito", 23)
print(f"Valor contador personas: {Persona.contador_personas}")
