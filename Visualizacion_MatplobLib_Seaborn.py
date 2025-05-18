import matplotlib.pyplot as plt
import pandas as pd

# Ejemplo de creación de un DataFrame con una columna 'edad'
df = pd.DataFrame({
	"edad": [23, 45, 56, 23, 34, 45, 67, 34, 23, 45, 56, 67, 34, 23, 45]
})

df["edad"].hist(bins=10)
plt.title("Distribución de edades")
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.show()
