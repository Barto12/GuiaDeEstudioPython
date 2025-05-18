import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crear un DataFrame simple
data = {
    "educacion": ["Primaria", "Secundaria", "Universidad", "Primaria", "Secundaria", "Universidad"],
    "ingreso": [1000, 1500, 2500, 1100, 1600, 2700]
}
df = pd.DataFrame(data)

# Graficar boxplot
sns.boxplot(x="educacion", y="ingreso", data=df)
plt.title("Ingreso por nivel educativo")
plt.show()
