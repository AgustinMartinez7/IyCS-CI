from fastapi import FastAPI
app = FastAPI()

def doble(numero: int) -> int:
    return numero * 2

@app.get("/doble")
def obtener_doble(numero: int):
    resultado = doble(numero)
    return {"resultado": resultado}

#var = "Taller CI/CD - Agustin Martinez"
#@app.get("/")
#def index():
#    return var