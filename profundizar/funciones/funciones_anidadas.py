# Funciones anidadas
def calculadora(a, b):
    # 1. Definir Funcion anidada
    def sumar(a, b):
        return a+b
    # 2. LLamamos a la funcion anidad
    print(sumar(a, b))



calculadora(4,5)