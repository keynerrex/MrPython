import json


class Rex:
    clas = 'Uno'
    count = 0

    @classmethod
    def aumentar_numero(self) -> int:
        Rex.count += 1
        return print(Rex.count)

    @classmethod
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs.get('args', None)
        if '123' in args:
            print('Pilla')
        elif '123' not in kwargs:
            print('Pilla')
        print(f"Construct: {args}")

    @classmethod
    async def hola(self, args):
        self.args = args
        print(args)

    def devolver_json(self):
        datos = {'nombre': 'nombre',
                 'apellido': 'apellido'}
        json.dumps(datos)
        return print(datos)


numero = Rex()
numero.aumentar_numero()
numero2 = Rex()
numero2.aumentar_numero()
numero2.devolver_json()
