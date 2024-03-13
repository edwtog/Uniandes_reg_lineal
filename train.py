import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

from joblib import dump

# Cargar los datos del archivo CSV
file_path = './data/student_scores.csv'
data = pd.read_csv(file_path)

# Visualizar las primeras filas del conjunto de datos para entender su estructura
#data.head()

# Preparar los datos para el entrenamiento del modelo
X = data[['Hours']]  # Variable independiente
y = data['Scores']  # Variable dependiente

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

#(mae, mse, rmse, r2)

# Guardar el modelo en un archivo
dump(model, 'modelo_regresion_lineal.joblib')