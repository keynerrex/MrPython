from prueba_logging import log


class Persona:

    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None) -> None:
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self) -> str:
        return f"""
            Id Persona: {self._id_persona}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Correo: {self._email}
        """

    @property
    def id_persona(self):
        return self._id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._email

    @correo.setter
    def correo(self, email):
        self._correo = email


# if __name__ == "__main__":
#     persona = Persona(19, "Keyner", "Oliveros", "keyner.com")

#     log.debug(persona)

#     # Simular un insert
#     persona2 = Persona(nombre="Keyner", apellido="Oliveros",
#                        email="keyner.com")
#     print(persona2)

#     # Simular un delete

# persona3 = Persona(id_persona=1)
# log.debug(persona3)
