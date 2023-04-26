from crearexcept import NumerosIdenticosException
resultado = None

try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))

    if a == b:
        raise NumerosIdenticosException("Numeros identicos")
    resultado = a/b
except Exception as e:
    print(f"Esception - Ha ocurrido un error: {e}, {type(e)}")
except ZeroDivisionError as e:
    print(f"Zero - Ocurrio un error: {e}, {type(e)}")
except TypeError as e:
    print(f"Type - Ocurrio un error: {e}, {type(e)}")

