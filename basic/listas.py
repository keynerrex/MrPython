# Listas -> []
["Keyner", "Bethoben", 19, 15]


frutas = []
frutas.append("Naranja")
frutas.append("Fresa")
frutas.append("Merengue")

print(frutas.sort())

print(frutas.pop())
# Iinsertae indice 0
print(frutas.insert(0, "Manzana"))

print(frutas)

print(frutas.insert(1, "Kiwi"))

# Elimina el ultimo valor agregado de la lista
frutas.pop(1)
print(frutas)

frutas.remove("Merengue")
print(frutas)
