from pydantic import BaseModel
from model.Galleta import Galleta

class Venta_Galleta(BaseModel):
    cantidad: int
    subtotal: float
    galleta: Galleta
