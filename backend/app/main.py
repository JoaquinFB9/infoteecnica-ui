# main.py

from fastapi import FastAPI

# 1. Creamos una instancia de FastAPI
# 'app' es el nombre estándar, es la variable que uvicorn buscará.
app = FastAPI(title="API InfotEEcnica", version="0.1.0")


# 2. Definimos nuestro primer "endpoint" o "ruta"
# El decorador @app.get("/") le dice a FastAPI que esta función
# manejará las peticiones GET a la raíz del sitio ("/")
@app.get("/")
def read_root():
    """
    Este es el endpoint principal de la API.
    Devuelve un saludo de bienvenida.
    """
    return {"message": "¡Hola, Ingeniero! Bienvenido al backend de tu visualizador."}