from fastapi import FastAPI,Body,Path,Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel,Field
from typing import Optional

##La libreria pydantic es para poder crear los esquemas de las clases, y para sanear los parametros que se mandan
## Importar Body es para poder recibr informacion en formato json
## HTMLResponse es para poder retornar html en nuestros procesos
## Optional, es para poder poner nuestras variables opcionales
## BaseModel es para poder crear esquemas con las clases
## Field es para poder sanear los campos en las clases
## Path sirve para sanear los campos donde se esta esperando un parametro de la rul movie/{id}
## Query es para sanear los campos que se envian como query movie?id=5?

##Se crea un endpoint

app = FastAPI()
app.title = "Mi app"
app.version="0.0.1"

class Movie(BaseModel):
    
    #id:int | None = None
    id:Optional[int] = None
    title:str = Field(max_length=15,min_length=5)
    overview:str=Field(max_length=15,min_length=5)
    year:str=Field(max_length=15,min_length=5)
    rating:float=Field(le=2022)
    category:str=Field(max_length=15,min_length=5)
    
    ##Con esta clase, se cargan los valores defaul de movies, debe de llamarse json_schema_extra, asi lo detecta la libreria
    class Config:
        json_schema_extra={
            "example":{
                "id":1,
                "title":"valor por defecto",
                "overview":"valor por defecto",
                "year":"valor por defecto",
                "rating":9.1,
                "category":"valor por defecto"
            }
        }


movies=[
    {
        'title': 'Avatar',
        'id': 1,
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    } ,
    {
        'id': 2,
        'title': 'Pulp Fiction',
        'overview': "Pulp Fiction es una película de crimen y drama que sigue las vidas entrecruzadas...",
        'year': '1994',
        'rating': 8.9,
        'category': 'Crimen'
    },
    {
        'id': 3,
        'title': 'El Señor de los Anillos: La Comunidad del Anillo',
        'overview': "En un mundo mágico, un grupo de aventureros emprende un viaje para destruir un anillo...",
        'year': '2001',
        'rating': 8.8,
        'category': 'Fantasía'
    },
    {
        'id': 3,
        'title': 'El Señor de los Anillos: La Comunidad del Anillo',
        'overview': "En un mundo mágico, un grupo de aventureros emprende un viaje para destruir un anillo...",
        'year': '2001',
        'rating': 8.8,
        'category': 'Fantasía'
    }
]

##NMetodos get
@app.get('/',tags=["Home"])
def message():
    #return {"hello":"word"}
    return HTMLResponse('<h1>Hola</h1>')


## Get con una ruta
@app.get('/movies',tags=['movies'])
def getmovies():
    return movies


##Get esperando parametros
@app.get('/movies/{id}',tags=["Movies"])
def getIdMovie(id:int = Path(ge=1,le=200)):
    
    for item in movies:
        print(item)
        if item['id']==id:
            return item
 
 
##Get con parametros query       
@app.get('/movies/',tags=['Movies'])
def getMoviesByCategory(category:str = Query(min_length=5,max_length=15)):
    
    for item in movies:
        if item['title']==category:
            return item
    
    return []
     
##Metodo post
@app.post('/post',tags=['Movies'])
def createMovie(id:int = Body(),title:str = Body(),overview:str=Body(),year:str=Body(),rating:int=Body(),category:str=Body()):
    
    movies.append(
        {
        'id':id,
        'title':title,
        'overview':overview,
        'year':year,
        'rating':rating,
        'category':category,
        }
    )
    
    return movies

##Metodo post v2
@app.post('/post2',tags=['Movies'])
def createMovie(movie:Movie):
    
    movies.append(movie)
    
    return movies


##Metodo delete
@app.delete('/delete/{id}',tags=['Movies'])
def deleteMovie(id:int):
    global movies
    movies=[pelicula for pelicula in movies if pelicula["id"]!=id ]
    
    return movies


##Metodo put version1
@app.put('/update',tags=['Movies'])
def updateMovie(id:int = Body(),title:str = Body()):
    
    for pelicula in movies:
        if pelicula["id"]==id:
            pelicula["title"]=title
    
    return movies


##Metodo put version2
@app.put('/update/{id}',tags=['Movies'])
def updateMovie2(id:int,title:str=Body()):
    
    for pelicula in movies:
        if pelicula["id"]==id:
            pelicula["title"]=title
    
    return movies    


##Metodo put version3
@app.put('/update2/{id}',tags=['Movies'])
def updateMovie2(id:int,movie:Movie):
    
    for pelicula in movies:
        if pelicula["id"]==id:
            pelicula["title"]=movie.title
            pelicula["overview"]=movie.overview
            pelicula["year"]=movie.year
            pelicula["rating"]=movie.rating
            pelicula["category"]=movie.category

    return movies    

