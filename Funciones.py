def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Luis"))  # Hola, Luis

# También se pueden definir funciones sin parámetros o con valores por defecto:

def bienvenida(mensaje="Bienvenido al curso"):
    print(mensaje)

bienvenida()
