mes_año = int(input("Escriba el mes del año: (1-12): "))

estacion = None

if mes_año == 1 or mes_año == 2 or mes_año == 12:
    estacion = "Invierno"
elif mes_año == 3 or mes_año == 4 or mes_año == 5:
    estacion = "Primavera"

elif mes_año == 6 or mes_año == 7 or mes_año == 9:
    estacion = "Verano"

elif mes_año == 9 or mes_año == 10 or mes_año == 11:
    estacion == "Otoño"

else:
    estacion = "Mes incorrecto"

print(f"Para el mes {mes_año} la estación es: {estacion}")
