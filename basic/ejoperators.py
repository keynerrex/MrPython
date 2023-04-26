valor = int(input("Digite el valor:"))
valor_minimo = 0
valor_maximo = 5


dentro_rango = valor >= valor_minimo and valor <= valor_maximo

if dentro_rango:
    print(f"El valor {valor} está dentro del rango")
else:
    print(f"El valor {valor} está fuera del rango")

# Con edades

age = int(input("Su edad es: "))

minimo_aplicar = 24
maximo_aplicar = 30

beneficio = age >= minimo_aplicar and age <= maximo_aplicar
if beneficio:
    print(
        f"Felicitaciones, ha sido beneficiario, su edad está dentro del rango{minimo_aplicar, maximo_aplicar}")
else:
    print(f"Sorry, no estas dentro del rango{minimo_aplicar, maximo_aplicar}")


# Asistir al partido

vacaciones = True
dia_descano = False

if vacaciones or dia_descano:
    print("Puede asistir al juego")
else:
    print("Tiene deberes por hacer")


# Operador not

if not (vacaciones or dia_descano):
    print("Tiene deberes por hacer")
else:
    print("Puede asistir al juego")

edad = 19
# Simplifcar and
if 20 <= edad < 30 or 30 <= edad < 40:
    print(edad)
