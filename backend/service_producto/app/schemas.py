from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombreProducto: str
    descripcionProducto: Optional[str] = None
    stockProducto: int
    precioProducto: float
    imagenProducto: Optional[str] = None
    categoriaProducto: str

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    idProducto: int

    class Config:
        from_attributes = True
