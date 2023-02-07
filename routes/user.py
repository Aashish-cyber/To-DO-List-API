from fastapi import APIRouter, HTTPException, Depends
from model.user import Todo 
from config.db import conn 
# from schemas.user import serializeDict, serializeList
from bson import ObjectId
from typing import Optional, List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
user = APIRouter() 

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")
@user.get("/token")
async def token_generate(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data)
    return {"access_token": form_data.username, "token_type": "bearer"}
# @user.post("/users/todo")
# async def create_todo(token: str = Depends(oauth_scheme)):
#     print(token)
#     return{
#         "user": "Aashish",
#         "todo": "my-work"
#     }

# Create, Read, Update, Delete

store_todo = []

@user.get('/')
async def home():
    return {"Hello": "World"}

@user.post('/todo/')
async def create_todo(token:str = Depends(oauth_scheme)):
    print(token)
    return{
        "user": "Aashish",
        "todo": "my_work"
    }

@user.get('/todo/', response_model=List[Todo])
async def get_all_todos(token:str = Depends(oauth_scheme)):
    print(token)
    return{
        "user": "Aashish",
        "todo": "my_work"
    }

@user.get('/todo/{id}')
async def get_todo(id: int):

    try:
        
        return store_todo[id]
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Not Found")

@user.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):

    try:

        store_todo[id] = todo
        return store_todo[id]
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Not Found")

@user.delete('/todo/{id}')
async def delete_todo(id: int):

    try:

        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    
    except:
        
        raise HTTPException(status_code=404, detail="Todo Not Found")




