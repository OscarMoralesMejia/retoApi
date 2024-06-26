from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
#from . import init as m
#import init as m
"""_summary_
uvicorn main:app --reload para ejecutar la api localmente
Tienes que estar en el directorio donde este el archivo main para poder levantar el servicio

"""
app = FastAPI()

"""Método inicial
"""
@app.get("/index")
def read_root():
    return {"message": "Bienvenido a mi API!"}

subapi = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@subapi.get("/sub")
def read_sub():
    return {"message": "This is a sub application"}

app.mount("/subapi", subapi)