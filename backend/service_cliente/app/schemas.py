from pydantic import BaseModel, EmailStr
from typing import Optional

class ClienteBase(BaseModel):
    cedula: int
    nombreCliente: str
    apellidoCliente: str
    correoCliente: EmailStr
    telefonoCliente: Optional[str] = None
    direccionCliente: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    cedula: Optional[int] = None
    nombreCliente: Optional[str] = None
    apellidoCliente: Optional[str] = None
    correoCliente: Optional[EmailStr] = None
    telefonoCliente: Optional[str] = None
    direccionCliente: Optional[str] = None

class Cliente(ClienteBase):
    idCliente: int

    class Config:
        from_attributes = True
