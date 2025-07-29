from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import date

class Factura(Base):
    __tablename__ = "facturas"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(String, unique=True, index=True)
    fecha = Column(Date, default=date.today)
    total = Column(Float, default=0.0)

    detalles = relationship("DetalleFactura", back_populates="factura", cascade="all, delete-orphan")

class DetalleFactura(Base):
    __tablename__ = "detalles_factura"

    id = Column(Integer, primary_key=True, index=True)
    factura_id = Column(Integer, ForeignKey("facturas.id"))
    cantidad = Column(Integer)
    precio_unitario = Column(Float)
    subtotal = Column(Float)

    factura = relationship("Factura", back_populates="detalles")
