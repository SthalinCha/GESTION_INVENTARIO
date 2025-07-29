from sqlalchemy import Column, Integer, String, Float, Text
from database import Base  # Tu clase declarativa

class Producto(Base):
    __tablename__ = "producto"

    idProducto = Column(Integer, primary_key=True, index=True)
    nombreProducto = Column(String(100), nullable=False)
    descripcionProducto = Column(Text, nullable=True)
    stockProducto = Column(Integer, nullable=False)
    precioProducto = Column(Float, nullable=False)
    imagenProducto = Column(String(255), nullable=True)  # Ruta de imagen
    categoriaProducto = Column(String(100), nullable=False)  # Categoría del producto
