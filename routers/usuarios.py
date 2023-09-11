from fastapi import APIRouter
from jwt_manager import create_token 
from fastapi.responses import HTMLResponse,JSONResponse
from schemas.usuario import User

usuarios_route = APIRouter()



##Metodo para loger
@usuarios_route.post('/login',tags=['auth'])
def login(user:User):
    
    if user.email=="admin@gmail.com" and user.password=="123":
       token:str  = create_token(user.dict())
       return JSONResponse(content=token)