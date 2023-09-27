import random

def generar_numero_colombiano():
    numero = "+57 3" + str(random.randint(0, 4))  # El segundo dígito será entre 0 y 4
    for _ in range(8):  # Genera 8 dígitos adicionales
        numero += str(random.randint(0, 9))
    return numero

def generar_100_numeros_colombianos():
    numeros = set()  # Usamos un conjunto para evitar repeticiones
    while len(numeros) < 10:
        numero = generar_numero_colombiano()
        numeros.add(numero)
    return numeros

if __name__ == "__main__":
    numeros_colombianos = generar_100_numeros_colombianos()
    for numero in numeros_colombianos:
        print(numero)
