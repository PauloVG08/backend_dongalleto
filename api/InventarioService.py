from fastapi.middleware.cors import CORSMiddleware
from api.GalletaService import app
from model.Inventario import Inventario
from controller.InventarioController import actualizarInventario, eliminarInventario, getAllInventarios, insertarInventario

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

@app.get("/inventario/getAll")
def apigetAllInventarios():
    try:
        response = getAllInventarios()
        return response
    except:
        print("ocurrió un error")

app.post("/inventario/insertar")
def apiinsertarInventario(inv: Inventario):
    try:
        response = insertarInventario(inv)
        return response
    except:
        print("ocurrió un error")

app.post("/inventario/actualizar")
def apiActualizarInventario(inv: Inventario):
    try:
        response = actualizarInventario(inv)
        return response
    except:
        print("ocurrió un error")

app.post("/inventario/eliminar")
def apiEliminarInventario(id: int):
    try:
        response = eliminarInventario(id)
        return response
    except:
        print("ocurrió un error")