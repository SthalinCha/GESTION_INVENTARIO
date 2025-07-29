from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Producto
from schemas import ProductoCreate, Producto
from crud import (
    obtener_productos, obtener_producto_por_id,
    crearNuevoProducto, actualizar_producto, eliminar_producto,
    buscar_productos
)
from cargadatosiniciales import cargar_productos_iniciales
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    cargar_productos_iniciales(db)
    db.close()

# Primero la ruta estática
@app.get("/productos/buscar", response_model=list[Producto])
def buscar(
    nombre: str | None = Query(default=None),
    categoria: str | None = Query(default=None),
    db: Session = Depends(get_db)
):
    resultados = buscar_productos(db, nombre=nombre, categoria=categoria)
    return resultados

# Luego la ruta dinámica
@app.get("/productos/{producto_id}", response_model=Producto)
def leer_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = obtener_producto_por_id(db, producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.get("/productos/", response_model=list[Producto])
def leer_productos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return obtener_productos(db, skip=skip, limit=limit)

@app.post("/productos/", response_model=Producto)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return crearNuevoProducto(db, producto.dict())

@app.put("/productos/{producto_id}", response_model=Producto)
def actualizar_producto_api(producto_id: int, producto: ProductoCreate, db: Session = Depends(get_db)):
    producto_actualizado = actualizar_producto(db, producto_id, producto)
    if producto_actualizado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_actualizado

@app.delete("/productos/{producto_id}", response_model=Producto)
def eliminar_producto_api(producto_id: int, db: Session = Depends(get_db)):
    producto_eliminado = eliminar_producto(db, producto_id)
    if producto_eliminado is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto_eliminado
