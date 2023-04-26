number = int(input("Ingrese un numero: "))

if number % 2 == 0:
    print(f"El {number} es par")
else:
    print(f"El {number} es impar")


# MAYOR DE EDAD

age = int(input("Ingrese su edad: "))
EDAD_REQUERIDA = 18
if age >= EDAD_REQUERIDA:
    print(f"Felicidades, tu edad cumple la edad requerida ({EDAD_REQUERIDA}) ")
elif age <= 0:
    print("Esta edad no esta permitida")
else:
    print(
        f"Lo siento pero no puedes pasar, tu edad no cumple la edad requerida ({EDAD_REQUERIDA}) ")
