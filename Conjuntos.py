numeros = {1, 2, 3, 3, 4}
print(numeros)  # {1, 2, 3, 4}
numeros.add(5)
numeros.remove(2)


# Operaciones utiles 
pares = {2, 4, 6}
impares = {1, 3, 5, 6}

print(pares.union(impares))        # Unión
print(pares.intersection(impares)) # Intersección
print(pares.difference(impares))   # Diferencia
