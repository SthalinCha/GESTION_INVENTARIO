from sqlalchemy.orm import Session
from app import models, schemas

def calcular_subtotal(cantidad, precio_unitario):
    return cantidad * precio_unitario

def calcular_total(detalles):
    return sum([calcular_subtotal(d.cantidad, d.precio_unitario) for d in detalles])

def crear_factura(db: Session, factura: schemas.FacturaCreate):
    total = calcular_total(factura.detalles)
    db_factura = models.Factura(numero=factura.numero, fecha=factura.fecha, total=total)

    for detalle in factura.detalles:
        subtotal = calcular_subtotal(detalle.cantidad, detalle.precio_unitario)
        db_detalle = models.DetalleFactura(
            cantidad=detalle.cantidad,
            precio_unitario=detalle.precio_unitario,
            subtotal=subtotal
        )
        db_factura.detalles.append(db_detalle)

    db.add(db_factura)
    db.commit()
    db.refresh(db_factura)
    return db_factura

def obtener_facturas(db: Session):
    return db.query(models.Factura).all()
