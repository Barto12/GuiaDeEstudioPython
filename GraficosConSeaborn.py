import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example DataFrame, replace with your actual data
df = pd.DataFrame({
	'genero': ['M', 'F', 'M', 'F'],
	'ingreso': [5000, 6000, 5500, 6500]
})

sns.boxplot(x="genero", y="ingreso", data=df)
plt.title("Ingreso por género")
plt.show()
