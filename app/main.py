from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/ping")
def ping():
    """Répond 'pong'"""
    return {"message": "pong"}


@app.get("/hello/{name}")
def say_hello(name: str):
    """Renvoie un message de bienvenue"""
    return {"message": f"Bonjour, {name} !"}


class AdditionRequest(BaseModel):
    a: float
    b: float


@app.post("/add")
def add_numbers(data: AdditionRequest):
    """Additionne deux nombres"""
    result = data.a + data.b
    return {"result": result}


class ReverseRequest(BaseModel):
    text: str


@app.post("/reverse")
def reverse_text(data: ReverseRequest):
    """Inverse une chaîne"""
    return {"reversed": data.text[::-1]}
