from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from app import models, schemas, crud, database, cargadatosiniciales

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

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    db = database.SessionLocal()
    try:
        cargadatosiniciales.cargar_facturas_iniciales(db)
    finally:
        db.close()

@app.post("/facturas/", response_model=schemas.Factura)
def crear_factura(factura: schemas.FacturaCreate, db: Session = Depends(get_db)):
    return crud.crear_factura(db, factura)

@app.get("/facturas/", response_model=list[schemas.Factura])
def listar_facturas(db: Session = Depends(get_db)):
    return crud.obtener_facturas(db)

@app.get("/facturas/{numero}", response_model=schemas.Factura)
def obtener_factura_por_numero(numero: str, db: Session = Depends(get_db)):
    factura = db.query(models.Factura).filter(models.Factura.numero == numero).first()
    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return factura
