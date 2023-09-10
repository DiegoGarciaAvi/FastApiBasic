from models.movie import Movie as MovieModel

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