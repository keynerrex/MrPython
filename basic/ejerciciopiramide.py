def piramide_suma(lim_min, lim_sup, margen=0):
    espacios_blancos = " " * margen
    print(espacios_blancos, lim_min, lim_sup)
    if lim_min > lim_sup:
        print(espacios_blancos, 0)
        return 0
    else:
        result = lim_min + piramide_suma(lim_min + 1, lim_sup, margen+4)
        print(espacios_blancos, result)
        return result


piramide_suma(2, 2)
