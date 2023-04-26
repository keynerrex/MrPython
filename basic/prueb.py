import math


def result():

    __calificacion__ = {
        1: "Mal",
        2: "Pésimo",
        3: "Regular",
        4: "Bien",
        5: "De lo mejor"
    }
    resultado = int(input("Como estuvo tu dia?"))
    if resultado > 5:
        print("La calificacion es hasta el 5")
    elif resultado <= 0:
        print("La calificacion no puede ser eso")

    if resultado == 1:
        return print(__calificacion__[1])
    elif resultado == 2:
        return print(__calificacion__[2])
    elif resultado == 3:
        return print(__calificacion__[3])
    elif resultado == 4:
        return print(__calificacion__[4])
    elif resultado == 5:
        return print(__calificacion__[5])


# Codigo resumido para que sea entendible
def resultmeth():
    __calificacion__ = {
        1: "Mal",
        2: "Pésimo",
        3: "Regular",
        4: "Bien",
        5: "De lo mejor"
    }

    resultado = int(input("Como estuvo tu dia? "))
    while resultado > 5 or resultado <= 0:
        resultado = int(
            input("Calificacion invalida. Introduce un valor entre 1 y 5: "))

    return print(__calificacion__[resultado])

# Dia de las semanas

def dia_semana():
    __dias__ = [
        "Lunes",
        "Martes",
        "Miercoles",
        "Jueves",
        "Viernes"
    ]

    dia_semana = input("Día de la semana:").capitalize()

    # si el input del dia no esta en la lista __dias__
    while dia_semana not in __dias__:
        dia_semana = input(
            "Dia Invalido, introduce uno correcto:").capitalize()

    return print(f"El dia de la semana es: {dia_semana}")


# print("El dia de la semana es: ", dia_semana)

# result()
resultmeth()
# dia_semana()
