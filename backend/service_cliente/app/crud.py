from sqlalchemy.orm import Session
from models import Cliente
from schemas import ClienteCreate, ClienteUpdate

def get_clientes(db: Session):
    return db.query(Cliente).all()

def get_cliente(db: Session, cliente_id: int):
    return db.query(Cliente).filter(Cliente.idCliente == cliente_id).first()

def create_cliente(db: Session, cliente: ClienteCreate):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def buscar_clientes_por_cedula(db: Session, cedula: str):
    return db.query(Cliente).filter(Cliente.cedula.contains(cedula)).all()

def update_cliente(db: Session, cliente_id: int, cliente_update: ClienteUpdate):
    db_cliente = get_cliente(db, cliente_id)
    if not db_cliente:
        return None
    for field, value in cliente_update.dict(exclude_unset=True).items():
        setattr(db_cliente, field, value)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = get_cliente(db, cliente_id)
    if not db_cliente:
        return None
    db.delete(db_cliente)
    db.commit()
    return db_cliente
