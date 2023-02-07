from fastapi import FastAPI, HTTPException
from routes.user import user 


app = FastAPI()
app = FastAPI(title="Todo API")
app.include_router(user)


