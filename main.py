from fastapi import  FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.usuarios import usuarios_route
##La libreria pydantic es para poder crear los esquemas de las clases, y para sanear los parametros que se mandan
## Importar Body es para poder recibr informacion en formato json
## HTMLResponse es para poder retornar html en nuestros procesos
## Optional, es para poder poner nuestras variables opcionales
## BaseModel es para poder crear esquemas con las clases
## Field es para poder sanear los campos en las clases
## Path sirve para sanear los campos donde se esta esperando un parametro de la rul movie/{id}
## Query es para sanear los campos que se envian como query movie?id=5?
## JsonResponse para enviar respuestas en formato json al cliente
## List es para poder retornar una lista
## HTTBearer es para el token
## Request es tener acceso a la peticion que viene del cliente
##Se crea un endpoint

app = FastAPI()
app.title = "Mi app"
app.version="0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(usuarios_route)

Base.metadata.create_all(bind=engine)






##NMetodos get
@app.get('/',tags=["Home"])
def message():
    #return {"hello":"word"}
    return HTMLResponse('<h1>Hola</h1>')

