from fastapi import FastAPI

app = FastAPI()

def doble(numero: int) -> int:
    return numero * 2

def doble(numero: int) -> int:
    return numero * 2

@app.get("/doble")
def obtener_doble(numero: int):
    resultado = doble(numero)
    return {"resultado": resultado}

