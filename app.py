from fastapi import FastAPI
import os

app = FastAPI()

def doble(numero: int) -> int:
    return numero * 2

@app.get("/doble")
def obtener_doble(numero: int):
    resultado = doble(numero)
    return {"resultado": resultado}

