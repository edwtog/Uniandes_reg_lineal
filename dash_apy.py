# Importar las librerías necesarias
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from joblib import load
import numpy as np

# Cargar el modelo entrenado
model = load('modelo_regresion_lineal.joblib')

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Predicción de Puntuaciones de Estudiantes'),

    html.Div(children='''
        Introduce las horas de estudio:
    '''),

    dcc.Input(id='input-hours', value='1', type='number', step=0.1),

    html.Button(id='submit-button', n_clicks=0, children='Predecir'),

    html.Div(id='output-prediction'),
])

# Callback para actualizar la predicción
@app.callback(
    Output('output-prediction', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('input-hours', 'value')]
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        hours = np.array([[float(value)]])
        predicted_score = model.predict(hours)[0]
        return f'La puntuación predicha para {value} horas de estudio es: {predicted_score:.2f}'
    else:
        return 'Ingrese las horas y haga clic en "Predecir".'

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
