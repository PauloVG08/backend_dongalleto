from pydantic import BaseModel
from model.Venta import Venta
from model.Venta_Galleta import Venta_Galleta
from typing import List

class DetalleVenta(BaseModel):
    venta: Venta
    lista_galleta: List[Venta_Galleta] = []
