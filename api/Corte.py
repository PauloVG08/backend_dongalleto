from fastapi.middleware.cors import CORSMiddleware
from model.Detalle_Venta import DetalleVenta
from model.Venta import Venta
from controller.Detalle_VentaController import generar_venta
from datetime import datetime
from controller.CorteController import getAllDetalleVenta
from api.VentaService import app


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

@app.post("/corte/getAll/{fecha}")
def apiInsertarVenta(fecha: str):
    try:
        # Asignar la fecha actual en el formato correcto
        response = getAllDetalleVenta(fecha)
        return response
    except Exception as e:  # Es una buena práctica capturar la excepción como 'e'
        print("Ocurrió un error:", e)
        print("ejemplo de nueva rama")