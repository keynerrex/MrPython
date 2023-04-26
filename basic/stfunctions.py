# def per(valor) -> str:
#     print(valor)


# per("xd")


# def test(a, b) -> int:
#     result = a + b
#     return result


# print(test(2, 3))
# lados = test(45, 6)
# print(lados)


# # default

# def div(a=4, b=5) -> int:
#     return a / b


# def lnombres(*nombres):
#     for nombre in nombres:
#         print(nombre)

# lnombres("Keyner","dsdf")


# def sumacion(*args):
#     resultado = 0
#     for valor in args:
#         resultado += valor
#     return resultado


# print(sumacion(3, 4, 5,))


def multipli(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado


print(multipli(4, 4))


def listardict(**dicts):
    for llave, valor in dicts.items():
        print(f"llave: {llave}, valor:{valor}")

listardict(message ="Hola")