from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from controller.GalletaController import getAllGalletas, insertarGalleta, eliminarGalleta, actualizarGalleta
from model.Galleta import Galleta

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5501"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/galleta/getAll")
def apigetAllCookies():
    try:
        response = getAllGalletas()
        return response
    except:
        print("ocurrió un error")

app.post("/galleta/insertar")
def insertarGalleta(galleta: Galleta):
    try:
        response = insertarGalleta(galleta)
        return response
    except:
        print("ocurrió un error")

app.post("/galleta/actualizar")
def apiActualizarGalleta(galleta: Galleta):
    try:
        response = actualizarGalleta(galleta)
        return response
    except:
        print("ocurrió un error")

app.post("/galleta/eliminar")
def apiEliminarGalleta(id: int):
    try:
        response = eliminarGalleta(id)
        return response
    except:
        print("ocurrió un error")
