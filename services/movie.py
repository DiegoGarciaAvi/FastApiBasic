from models.movie import Movie as MovieModel
from schemas.movie import Movie
class MovieService():
    
    def __init__(self,db)-> None:
        self.db=db
        
    def getMovies(self):
        result = self.db.query(MovieModel).all()
        return result
    
    def getMovie(self,id):
        result  = self.db.query(MovieModel).filter(MovieModel.id==id).first()
        return result
    
    
    def getMovieByCategori(self,category):
        result = self.db.query(MovieModel).filter(MovieModel.category==category).all()
        return result
    
    def guardarMovie(self,movie:Movie):
        new_movie=MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return "Exito"
    
    def upadteMovie(self,id:int,movie:Movie):
        
        result = self.db.query(MovieModel).filter(MovieModel.id==id).first()
        
        result.title=movie.title
        result.overview=movie.overview
        result.year=movie.year
        result.rating=movie.rating
        result.category=movie.category
        self.db.commit()
    
        return  
    
    def deleteMovie(self,id:int):
        
        result= self.db.query(MovieModel).filter(MovieModel.id==id).first()
        self.db.delete(result)
        self.db.commit()
        
        return