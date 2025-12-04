from fastapi import FastAPI 
from app.api import auth

app = FastAPI()


@app.get("/")
def root_gateway():
    return {"message":"gateway service active!"}

@app.include_router(auth.router)
