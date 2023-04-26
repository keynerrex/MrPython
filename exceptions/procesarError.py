from crearexcept import NumerosIdenticosException
resultado = None
a = 10
b = 2
try:
    resultado = a / b
except Exception as e:
    print(f"Esception - Ha ocurrido un error: {e}, {type(e)}")
except ZeroDivisionError as e:
    print(f"Zero - Ocurrio un error: {e}, {type(e)}")
except TypeError as e:
    print(f"Type - Ocurrio un error: {e}, {type(e)}")

print(f"Resultado: {resultado}")
print("Continuamos....")
