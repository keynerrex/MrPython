# Profundizando en listas, son editables
nombres = ['keyner', 'santiago']
nombres2 = "oliveros florez".split()
# Sumar listas
print(f"sumar: {nombres+nombres2}")

# extender
nombres.extend(nombres2)
print(f"nn: {nombres}")

# Incluir separador
numeros = [1, 2, 3]
print(*numeros, sep="-")

# Funcion zip
mezcla = zip(numeros, nombres)
print(list(mezcla))
