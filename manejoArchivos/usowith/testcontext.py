from contextmanager import ManejoArchivos
with ManejoArchivos("keyner.txt") as archivo:
    print(archivo.read())
 