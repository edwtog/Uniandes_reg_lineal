# FastAPI ML Model Deployment Example

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3101/)

Este repositorio contiene un ejemplo básico de cómo crear una API utilizando FastAPI para desplegar un modelo de machine learning. En este ejemplo, se utiliza un modelo de regresión para demostrar el proceso de implementación de una API utilizando FastAPI.

Además, incluye ejemplos de interfaces de usuario generadas con Streamlit y Dash para interactuar con el modelo.

## Requisitos

Antes de ejecutar el código en este repositorio, asegúrate de tener instalado lo siguiente:

- Python (preferiblemente Python 3.10 o superior)
- pip (gestor de paquetes de Python)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Streamlit](https://streamlit.io/)
- [Dash](https://dash.plotly.com/)

Puedes instalar los requisitos utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```

El servidor se inicia con el comando

```bash
uvicorn apy:app --reload
```

Para realizar una predicción desde otra terminal:

```bash
curl -X POST "http://127.0.0.1:8000/predict/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"hours\": 5.0}"
```
