from fastapi import APIRouter
from fastapi import Depends, FastAPI,Body, HTTPException,Path,Query,Request
from fastapi.responses import HTMLResponse,JSONResponse
from typing import List
from config.database import Session,engine,Base
from models.movie import Movie as MovieModel 
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from jwt_manager import create_token, validate_token
from services.movie import MovieService
from schemas.movie import Movie

movie_router=APIRouter()

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


##Metodo get con Json y indicando que se regresa una lista
@movie_router.get('/moviesList', tags=['Movies'],response_model=List[Movie])
def getMoviesJson() -> List[Movie]:
    return JSONResponse(content=movies)

## Get con una ruta
@movie_router.get('/movies',tags=['movies'])
def getmovies():
    return movies


##Get esperando parametros
@movie_router.get('/movies/{id}',tags=["Movies"])
def getIdMovie(id:int = Path(ge=1,le=200)):
    
    db = Session()
    #result= db.query(MovieModel).filter(MovieModel.id==id).first()
    result= MovieService(db).getMovie(id)
    if not result:
        return JSONResponse(content={"message":"No existe"})
    return JSONResponse(content=jsonable_encoder(result))
    
    f""" or item in movies:
        print(item)
        if item['id']==id:
            return item """
 
 
##Get regresando una Movie usando la importancion List
@movie_router.get('/movies/{id}',tags=["Movies"],response_model=Movie)
def getIdMovie(id:int = Path(ge=1,le=200)) ->Movie:
    
    for item in movies:
        print(item)
        if item['id']==id:
            return JSONResponse(item)
 
  
##Get con parametros query       
@movie_router.get('/movies/',tags=['Movies'])
def getMoviesByCategory(category:str = Query(min_length=5,max_length=15)):
    
    db = Session()
    result=MovieService(db).getMovieByCategori(category)
    if not result:
        return JSONResponse(content={"messagge:":"No encotrado"})
    return JSONResponse(content=jsonable_encoder(result))
    
    """ for item in movies:
        if item['title']==category:
            return item
    
    return [] """
    
    
##Metodo get con Json
@movie_router.get('/moviesJson', tags=['Movies'],dependencies=[Depends(JWTBearer())] )
def getMoviesJson():
    db = Session()
    result= MovieService(db).getMovies()
    #result=db.query(MovieModel).all()
   # return JSONResponse(content=movies)
    return JSONResponse(content=jsonable_encoder(result))
    
    
##Metodo post
@movie_router.post('/post',tags=['Movies'])
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
@movie_router.post('/post2',tags=['Movies'])
def createMovie(movie:Movie):
    
    ##Pasar datos haciendo la conexion a db
    
    db= Session()
#    MovieModel(title=movie.title)
    MovieService(db).guardarMovie(movie)
    
    #movies.append(movie)
    
    #return movies
    return JSONResponse(content={"message":"Registro correcto"})

##Metodo delete
@movie_router.delete('/delete/{id}',tags=['Movies'])
def deleteMovie(id:int):
    
    db=Session()
    result=MovieService(db).getMovie(id)
    if not result:
        return JSONResponse(content={"message":"No encontrado"})
    
    MovieService(db).deleteMovie(id)
    return JSONResponse(content={"Message":"Exito eliminando"})    
    """ global movies
    movies=[pelicula for pelicula in movies if pelicula["id"]!=id ]
    
    return movies """


##Metodo put version1
@movie_router.put('/update',tags=['Movies'])
def updateMovie(id:int = Body(),title:str = Body()):
    
    for pelicula in movies:
        if pelicula["id"]==id:
            pelicula["title"]=title
    
    return movies


##Metodo put version2
@movie_router.put('/update/{id}',tags=['Movies'])
def updateMovie2(id:int,title:str=Body()):
      
    for pelicula in movies:
        if pelicula["id"]==id:
            pelicula["title"]=title
    
    return movies    
 

##Metodo put version3
@movie_router.put('/update2/{id}',tags=['Movies'])
def updateMovie2(id:int,movie:Movie):
    
    db = Session()
    result = MovieService(db).getMovie(id)
    

    if not result :
        return JSONResponse(content={"Mesagge":"No encotrado"})
    
    MovieService(db).upadteMovie(id,movie)
    
    return JSONResponse(content={"message":"Extio"})
    
    """ for pelicula in movies:
        if pelicula["id"]==id:
            pelicula["title"]=movie.title
            pelicula["overview"]=movie.overview
            pelicula["year"]=movie.year
            pelicula["rating"]=movie.rating
            pelicula["category"]=movie.category

    return movies    """ 

