cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

#Comprension de diccionarios

edades = {"Ana": 20, "Luis": 25, "Sofía": 23}
mayores = {k: v for k, v in edades.items() if v >= 23}
print(mayores)  # {'Luis': 25, 'Sofía': 23}
