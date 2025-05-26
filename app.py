from fastapi import FastAPI

app = FastAPI()

def doble(numero: int) -> int:
    return numero * 3

@app.get("/doble")
def obtener_doble(numero: int):
    resultado = doble(numero)
    return {"resultado": resultado}
