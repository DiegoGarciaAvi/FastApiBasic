1.- Instalar el entorno virual
    python -m venv venv
2.- Activamos el entorno virual
    soruce venv/bin/activate
3.- Instalamos fastapi
    pip install fastapi
4.- Instalamos el modulo para poder ejecutar la aplicacion de api
    pip install uvicorn

5.- Estructura basica de main
    from fastapi import FastAPI

    app = FastAPI()

    ##Se crea un endpoint

    @app.get('/')
    def message():
        return "Hola mundo"    

6.- Se inicia el proyecto 
    uvicorn main:app --reload --port 8000