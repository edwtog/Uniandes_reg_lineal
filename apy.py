from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from joblib import load

# Cargar el modelo previamente guardado
model = load('modelo_regresion_lineal.joblib')

# Inicializar FastAPI
app = FastAPI()

# Modelo de solicitud para recibir las horas de estudio
class RequestModel(BaseModel):
    hours: float

# Ruta de predicción
@app.post("/predict/")
async def predict(request_model: RequestModel):
    hours = np.array([[request_model.hours]])
    score_pred = model.predict(hours)
    return {"predicted_score": score_pred[0]}

# Ejemplo de cómo correr uvicorn desde el script, aunque se recomienda ejecutarlo desde la línea de comando
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

