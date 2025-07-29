from sqlalchemy.orm import Session
from models import Producto
from schemas import ProductoCreate

def validarExistenciaInicial(db: Session) -> bool:
    return db.query(Producto).first() is not None

def crearNuevoProducto(db: Session, producto_dict: dict):
    nuevo_producto = Producto(
        nombreProducto=producto_dict["nombreProducto"],
        descripcionProducto=producto_dict.get("descripcionProducto", ""),
        stockProducto=producto_dict["stockProducto"],
        precioProducto=producto_dict["precioProducto"],
        imagenProducto=producto_dict.get("imagenProducto", None),
        categoriaProducto=producto_dict["categoriaProducto"]
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

def obtener_productos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Producto).offset(skip).limit(limit).all()

def obtener_producto_por_id(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.idProducto == producto_id).first()

def actualizar_producto(db: Session, producto_id: int, datos_actualizados: ProductoCreate):
    producto = db.query(Producto).filter(Producto.idProducto == producto_id).first()
    if producto:
        producto.nombreProducto = datos_actualizados.nombreProducto
        producto.descripcionProducto = datos_actualizados.descripcionProducto
        producto.stockProducto = datos_actualizados.stockProducto
        producto.precioProducto = datos_actualizados.precioProducto
        producto.imagenProducto = datos_actualizados.imagenProducto
        producto.categoriaProducto = datos_actualizados.categoriaProducto
        db.commit()
        db.refresh(producto)
    return producto

def eliminar_producto(db: Session, producto_id: int):
    producto = db.query(Producto).filter(Producto.idProducto == producto_id).first()
    if producto:
        db.delete(producto)
        db.commit()
    return producto

def buscar_productos(db: Session, nombre: str = None, categoria: str = None):
    query = db.query(Producto)
    if nombre:
        query = query.filter(Producto.nombreProducto.ilike(f"%{nombre}%"))
    if categoria and categoria.lower() != "todos":
        query = query.filter(Producto.categoriaProducto.ilike(f"%{categoria}%"))
    return query.all()
