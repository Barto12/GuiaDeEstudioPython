from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar datos
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)

# Modelo
modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# Evaluar
predicciones = modelo.predict(X_test)
print("Precisión:", accuracy_score(y_test, predicciones))
