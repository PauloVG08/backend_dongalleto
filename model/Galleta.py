from pydantic import BaseModel

class Galleta(BaseModel):
    idGalleta: int
    nombre: str
    descripcion: str
    precio: float
    cantidad: int
    img: str
    estatus: int