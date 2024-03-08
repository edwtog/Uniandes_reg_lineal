import streamlit as st
from joblib import load
import numpy as np
import os

# Cargar el modelo entrenado
model = load('modelo_regresion_lineal.joblib')

# Crear la interfaz de la aplicación con Streamlit
st.title('Predicción de Puntuaciones de Estudiantes')

# Entrada del usuario para las horas de estudio
hours = st.number_input('Introduce las horas de estudio:', min_value=0.0, max_value=24.0, value=1.0, step=0.1)

# Botón para realizar la predicción
if st.button('Predecir Puntuación'):
    # Realizar la predicción
    predicted_score = model.predict(np.array([[hours]]))[0]
    # Mostrar la predicción
    st.write(f'La puntuación predicha para {hours} horas de estudio es: {predicted_score:.2f}')

# Instrucciones para ejecutar la aplicación (agregar al final del script)
# st.write('Para ejecutar esta aplicación, utiliza el siguiente comando en tu terminal:')
# st.code('streamlit run app.py')
