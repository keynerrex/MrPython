try:
    10/0
except Exception as e:
    print(f"Ocurrio un error: {e}")

try:
    10/0
except ZeroDivisionError as e:
    print(f"Ocurrio un error: {e}")