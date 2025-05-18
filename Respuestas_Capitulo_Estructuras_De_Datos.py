# Lista inicial de comidas favoritas
comidas_favoritas = ["pizza", "tacos", "sushi", "hamburguesa"]

# Agregar una comida nueva
comidas_favoritas.append("pasta")

# Eliminar una comida
comidas_favoritas.remove("sushi")

# Mostrar la lista actualizada
print("Lista actualizada de comidas favoritas:")
print(comidas_favoritas)

# Declaración de una tupla con latitud y longitud
coordenadas = (19.4326, -99.1332)  # Ejemplo: Ciudad de México

# Acceso a cada valor por separado
latitud = coordenadas[0]
longitud = coordenadas[1]

print("Latitud:", latitud)
print("Longitud:", longitud)

# Hobbies propios
mis_hobbies = {"leer", "correr", "dibujar", "programar"}

# Hobbies de un amigo
hobbies_amigo = {"cocinar", "leer", "programar", "bailar"}

# Hobbies en común
hobbies_comunes = mis_hobbies.intersection(hobbies_amigo)

print("Hobbies en común con mi amigo:")
print(hobbies_comunes)

# Crear un diccionario con datos del estudiante
estudiante = {
    "nombre": "Luis",
    "edad": 21,
    "carrera": "Ingeniería en Sistemas",
    "promedio": 8.5
}

# Mostrar todos los datos
print("Datos del estudiante:")
print(estudiante)

# Actualizar el promedio
estudiante["promedio"] = 9.0

print("Promedio actualizado:")
print(estudiante["promedio"])
