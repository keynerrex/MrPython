letras = ["a", "b", "c", "d", "e", "f"]

for letra in letras:
    print(letra)
    if letra == letras[0]:
        print(letra)


# break
for palabra in "Colombia":
    if palabra == "o":
        print(f"Letra encontrada: {palabra}")

else:
    print("Fin ")


# continue
for i in range(6):
    if i % 2 == 0:
        print(f"Valor: {i}")
        continue


for value in range(6):
    if value % 2 != 0:
        continue
    print(f"Valor: {value}")
