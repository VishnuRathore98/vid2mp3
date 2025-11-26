from fastapi import FastAPI
from app.api.routes import user_routes

app = FastAPI()


@app.get("/")
def root():
    return {"message": "auth service"}


app.include_router(user_routes.router)
