from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field

class DetalleFacturaCreate(BaseModel):
    cantidad: int = Field(..., gt=0)
    precio_unitario: float = Field(..., gt=0)

class DetalleFactura(DetalleFacturaCreate):
    id: int
    subtotal: float

    class Config:
        from_attributes = True

class FacturaCreate(BaseModel):
    numero: str
    fecha: Optional[date] = None
    detalles: List[DetalleFacturaCreate]

class Factura(BaseModel):
    id: int
    numero: str
    fecha: date
    total: float
    detalles: List[DetalleFactura]

    class Config:
        from_attributes = True
