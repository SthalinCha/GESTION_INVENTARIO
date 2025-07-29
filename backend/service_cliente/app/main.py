from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
import crud
import schemas
from fastapi.middleware.cors import CORSMiddleware

# Importa la función para cargar datos iniciales
from cargadatosiniciales import cargar_clientes_iniciales

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar CORS (ajusta los orígenes según tu frontend)
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

# Dependencia para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Evento startup para cargar datos iniciales
@app.on_event("startup")
def startup_event():
    db = SessionLocal()
    try:
        cargar_clientes_iniciales(db)
    finally:
        db.close()

# Rutas para clientes

# Listar todos los clientes
@app.get("/clientes/", response_model=list[schemas.Cliente])
def leer_clientes(db: Session = Depends(get_db)):
    clientes = crud.get_clientes(db)
    return clientes

# Buscar clientes por parte de cédula
@app.get("/clientes/buscar", response_model=list[schemas.Cliente])
def buscar_clientes(cedula: str = Query(..., description="Parte de la cédula para buscar"), db: Session = Depends(get_db)):
    clientes = crud.buscar_clientes_por_cedula(db, cedula)
    return clientes

# Obtener cliente por ID
@app.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
def leer_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.get_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# Buscar cliente por cédula exacta
@app.get("/clientes/cedula/{cedula}", response_model=schemas.Cliente)
def leer_cliente_por_cedula(cedula: str, db: Session = Depends(get_db)):
    cliente = crud.buscar_cliente_por_cedula(db, cedula)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# Crear cliente
@app.post("/clientes/", response_model=schemas.Cliente)
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db, cliente)

# Actualizar cliente
@app.put("/clientes/{cliente_id}", response_model=schemas.Cliente)
def actualizar_cliente(cliente_id: int, cliente_update: schemas.ClienteUpdate, db: Session = Depends(get_db)):
    cliente_actualizado = crud.update_cliente(db, cliente_id, cliente_update)
    if not cliente_actualizado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_actualizado

# Eliminar cliente
@app.delete("/clientes/{cliente_id}", response_model=schemas.Cliente)
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente_eliminado = crud.delete_cliente(db, cliente_id)
    if not cliente_eliminado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente_eliminado
