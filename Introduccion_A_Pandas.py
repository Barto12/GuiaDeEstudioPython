import pandas as pd

df = pd.read_csv("archivo.csv")
print(df.head())  # Muestra las primeras filas
print(df.shape)        # Filas y columnas
print(df.columns)      # Nombres de columnas
print(df.describe())   # Estadísticas básicas
print(df.info())       # Tipos de datos y valores nulos
df = df.dropna()               # Elimina filas con valores nulos
df = df.fillna(0)              # Sustituye nulos por 0
print(df.duplicated().sum())   # Cuenta registros duplicados

print(df["edad"])              # Columna específica
print(df[["nombre", "edad"]])  # Varias columnas
print(df.iloc[0:5])            # Primeras 5 filas (por índice)
print(df[df["edad"] > 30])     # Filtro condicional

print(df.groupby("ciudad")["ingreso"].mean())  # Promedio de ingreso por ciudad

