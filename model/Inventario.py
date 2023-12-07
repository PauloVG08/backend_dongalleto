from pydantic import BaseModel
from datetime import date  

class Inventario(BaseModel):
    idInventario: int
    cantidad: float
    nombre: str
    caducidad: date
    estatus: int