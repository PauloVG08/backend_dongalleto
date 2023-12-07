from fastapi.middleware.cors import CORSMiddleware
from api.GalletaService import app
from model.Detalle_Venta import DetalleVenta
from model.Venta import Venta
from controller.Detalle_VentaController import generar_venta

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

app.post("/detalle_venta/insertar")
def apiInsertarVenta(dv: DetalleVenta):
    try:
        response = generar_venta(dv)
        return response
    except:
        print("ocurrió un error")
