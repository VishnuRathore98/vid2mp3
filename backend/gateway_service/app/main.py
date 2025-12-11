from fastapi import FastAPI 
from app.api.v1 import auth, file

app = FastAPI()


@app.get("/")
def root_gateway():
    return {"message":"gateway service active!"}

@app.include_router(auth.router)
@app.include_router(file.router)
