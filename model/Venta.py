from pydantic import BaseModel

class Venta(BaseModel):
    idVenta: int
    fecha: str
    total: float
