# Definición de la función
def calcular_promedio(num1, num2):
    promedio = (num1 + num2) / 2
    return promedio

# Ejemplo de uso
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

resultado = calcular_promedio(numero1, numero2)
print(f"El promedio es: {resultado}")
