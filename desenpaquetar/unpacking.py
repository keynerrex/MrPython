# Desenpaquetar -Unpacking
valores = 1, 2, 3
print(type(valores))

# Definiendo tupla de valores
valor1, valor2, valor3 = 1, 2, 3

print(valor1, valor2, valor3)

#   Se omite el uso
valor1, _, valor3 = 1, 2, 3

# Asignar varios a uno
valor1, *valor2 = 1, 2, 3, 4, 5
print(valor1, valor2)
