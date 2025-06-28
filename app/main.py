import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI


app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}
