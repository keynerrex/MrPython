
def area(alto, ancho):
    area = alto*ancho
    return print(f"El area es: {area}")


def perimetro(alto, ancho):
    perimetro = (alto*ancho)*2
    return print(f"El perimetro es: {perimetro}")


saber = int(input("Que desea calcular?\n1.Area \n2.Perimetro\n"))
ancho = int(input("Digite el ancho:"))
alto = int(input("Digite el alto:"))

if saber == 1:
    area(alto, ancho)
else:
    perimetro(alto, ancho)
