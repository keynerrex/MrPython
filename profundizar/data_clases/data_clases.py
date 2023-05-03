from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0


@dataclass(eq=True, frozen=True)
class Persona:

    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    # Despues del __init__
    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f"Nombre vacío: {self.nombre}")


domicilio1 = Domicilio("calle 45", 324)
persona = Persona("keyner", "oliveros", domicilio1)
print(f"{persona!r}")

# Variable de clase
print(f"Persona: {persona.contador_personas}")
# VaRIABLES de instancia
print(f"Persona instancia: {persona.__dict__}")

# Valores vacios
# persona_nada = Persona("", "")
# print(persona_nada)


# Revisar igualdad entre objetos
persona2 = Persona("Kina", "YT", Domicilio("calle 54", 300))
print(f"Objetos iguales? :{persona == persona2} ")


# Agregar a una coleccion
coleccion = {persona, persona2}
print(coleccion)
# No se puede
# coleccion[0].nombre = "nuevokeyner"
