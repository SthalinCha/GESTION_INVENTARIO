from sqlalchemy import Column, Integer, String
from database import Base  # o de donde importes la base

class Cliente(Base):
    __tablename__ = "clientes"
    idCliente = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True, nullable=False)
    nombreCliente = Column(String, nullable=False)
    apellidoCliente = Column(String, nullable=False)
    correoCliente = Column(String, unique=True, index=True, nullable=False)
    telefonoCliente = Column(String, nullable=True)
    direccionCliente = Column(String, nullable=True)
