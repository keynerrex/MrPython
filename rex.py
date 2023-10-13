class Rex:
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs.get('args', None)
        if '123' in args:
            print('Pilla')
        elif '123' not in kwargs:
            print('Pilla')
        print(f"Construct: {args}")


uno = Rex('fdsfd', 'dfdsfds', 'fdsfsdf', 'rregfr', 64654, '123')
