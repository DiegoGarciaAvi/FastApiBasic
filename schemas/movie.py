from pydantic import BaseModel,Field
from typing import Optional

class Movie(BaseModel):
    
    #id:int | None = None
    id:Optional[int] = None
    title:str = Field(max_length=15,min_length=5)
    overview:str=Field(max_length=15,min_length=5)
    year:str=Field(max_length=15,min_length=2)
    rating:float=Field(le=2022)
    category:str=Field(max_length=15,min_length=5)
    
    ##Con esta clase, se cargan los valores defaul de movies, debe de llamarse json_schema_extra, asi lo detecta la libreria
    class Config:
        json_schema_extra={
            "example":{
                "id":1,
                "title":"My titulo",
                "overview":"Reseña",
                "year":"2022",
                "rating":9.1,
                "category":"Categoria"
            }
        }
