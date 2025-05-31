from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

def doble(numero: int) -> int:
    return numero * 2

@app.get("/doble_html", response_class=HTMLResponse)
def obtener_doble_html(request: Request, numero: int):
    resultado = doble(numero)
    return templates.TemplateResponse("doble.html", {
        "request": request,
        "numero": numero,
        "resultado": resultado
    })
