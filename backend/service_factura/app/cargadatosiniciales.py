from sqlalchemy.orm import Session
from datetime import date
from app.models import Factura, DetalleFactura

def cargar_facturas_iniciales(db: Session):
    if db.query(Factura).count() == 0:
        facturas_data = [
            {
                "numero": "F000001",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 2, "precio_unitario": 15.0, "subtotal": 30.0},
                    {"cantidad": 1, "precio_unitario": 45.0, "subtotal": 45.0}
                ],
            },
            {
                "numero": "F000002",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 5, "precio_unitario": 8.0, "subtotal": 40.0},
                ],
            },
            {
                "numero": "F000003",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 3, "precio_unitario": 12.5, "subtotal": 37.5},
                    {"cantidad": 4, "precio_unitario": 6.0, "subtotal": 24.0},
                ],
            },
            {
                "numero": "F000004",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 10, "precio_unitario": 5.0, "subtotal": 50.0},
                    {"cantidad": 2, "precio_unitario": 20.0, "subtotal": 40.0},
                ],
            },
            {
                "numero": "F000005",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 1, "precio_unitario": 100.0, "subtotal": 100.0},
                ],
            },
            {
                "numero": "F000006",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 6, "precio_unitario": 7.5, "subtotal": 45.0},
                    {"cantidad": 3, "precio_unitario": 15.0, "subtotal": 45.0},
                ],
            },
            {
                "numero": "F000007",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 2, "precio_unitario": 25.0, "subtotal": 50.0},
                ],
            },
            {
                "numero": "F000008",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 8, "precio_unitario": 3.5, "subtotal": 28.0},
                    {"cantidad": 4, "precio_unitario": 12.0, "subtotal": 48.0},
                ],
            },
            {
                "numero": "F000009",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 1, "precio_unitario": 200.0, "subtotal": 200.0},
                ],
            },
            {
                "numero": "F000010",
                "fecha": date.today(),
                "detalles": [
                    {"cantidad": 3, "precio_unitario": 30.0, "subtotal": 90.0},
                    {"cantidad": 2, "precio_unitario": 10.0, "subtotal": 20.0},
                    {"cantidad": 1, "precio_unitario": 50.0, "subtotal": 50.0},
                ],
            },
        ]

        for fdata in facturas_data:
            detalles_objs = [DetalleFactura(**d) for d in fdata.pop("detalles")]
            total = sum(d.subtotal for d in detalles_objs)
            factura = Factura(**fdata, total=total, detalles=detalles_objs)
            db.add(factura)

        db.commit()
        print("Facturas cargadas correctamente")
