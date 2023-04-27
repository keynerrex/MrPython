try:
    archivotxt = open("keyner.txt", "w", encoding="utf-8")
    archivotxt.write("Bienvenido keyner\nAdiós Keyner")
except Exception as e:
    print(e)
finally:
    archivotxt.close()
    print("Fin de escritura...")
