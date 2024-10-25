from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hola desde FastAPI!"}

@app.get("/hello/{name}")
async def root(name: str):
    return {"message": f"Hola {name} desde FastAPI!"}

handler = Mangum(app)