from sqlalchemy.orm import Session
from models import Producto
def cargar_productos_iniciales(db: Session):
    if db.query(Producto).count() == 0:
        productos = [

            # === CONSTRUCCIÓN ===
            {"nombreProducto": "Placa de yeso STANDAR", "descripcionProducto": "Placa de yeso para interiores 1.22 x 2.44 m", "stockProducto": 25, "precioProducto": 9.99, "imagenProducto": "imagenes/c1.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Impermeabilizante ADIFORCE", "descripcionProducto": "Impermeabilizante elastomérico flexible", "stockProducto": 18, "precioProducto": 29.16, "imagenProducto": "imagenes/c2.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Bondex Plus 25kg - INTACO", "descripcionProducto": "Mortero modificado con polímeros", "stockProducto": 30, "precioProducto": 7.55, "imagenProducto": "imagenes/c3.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Cemento Portland GU", "descripcionProducto": "Cemento general para construcción", "stockProducto": 100, "precioProducto": 6.75, "imagenProducto": "imagenes/c4.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Arena lavada m3", "descripcionProducto": "Arena para mezcla de concreto", "stockProducto": 50, "precioProducto": 12.00, "imagenProducto": "imagenes/c5.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Grava 3/4 m3", "descripcionProducto": "Piedra triturada para hormigón", "stockProducto": 40, "precioProducto": 14.50, "imagenProducto": "imagenes/c6.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Varilla de acero 3/8", "descripcionProducto": "Varilla de refuerzo estructural", "stockProducto": 200, "precioProducto": 3.80, "imagenProducto": "imagenes/c7.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Bloque de concreto 10x20x40", "descripcionProducto": "Bloque estructural para muro", "stockProducto": 500, "precioProducto": 0.68, "imagenProducto": "imagenes/c8.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Malla electrosoldada", "descripcionProducto": "Reforzamiento de losas y muros", "stockProducto": 80, "precioProducto": 19.90, "imagenProducto": "imagenes/c9.png", "categoriaProducto": "Construcción"},
            {"nombreProducto": "Tubo PVC 1/2 pulgada", "descripcionProducto": "Tubo para instalación sanitaria", "stockProducto": 120, "precioProducto": 1.60, "imagenProducto": "imagenes/c10.png", "categoriaProducto": "Construcción"},

            # === HERRAMIENTAS ELÉCTRICAS ===
            {"nombreProducto": "Mini amoladora GWS 700", "descripcionProducto": "Amoladora BOSCH profesional", "stockProducto": 15, "precioProducto": 36.81, "imagenProducto": "imagenes/e1.png", "categoriaProducto": "Herramientas Eléctricas"},
            {"nombreProducto": "Taladro inalámbrico 12V", "descripcionProducto": "Taladro 3/8\" PRETUL", "stockProducto": 20, "precioProducto": 44.35, "imagenProducto": "imagenes/e2.png", "categoriaProducto": "Herramientas Eléctricas"},
            {"nombreProducto": "Lijadora orbital 1/4 hoja", "descripcionProducto": "Lijadora eléctrica de palma", "stockProducto": 10, "precioProducto": 32.00, "imagenProducto": "imagenes/e3.png", "categoriaProducto": "Herramientas Eléctricas"},
            {"nombreProducto": "Sierra circular 7 1/4\"", "descripcionProducto": "Sierra eléctrica 1400W", "stockProducto": 12, "precioProducto": 67.00, "imagenProducto": "imagenes/e4.png", "categoriaProducto": "Herramientas Eléctricas"},
            {"nombreProducto": "Rotomartillo 800W", "descripcionProducto": "Perforación en concreto y ladrillo", "stockProducto": 8, "precioProducto": 74.90, "imagenProducto": "imagenes/e5.png", "categoriaProducto": "Herramientas Eléctricas"},
            {"nombreProducto": "Multímetro digital", "descripcionProducto": "Medición de voltaje y corriente", "stockProducto": 25, "precioProducto": 9.95, "imagenProducto": "imagenes/e6.png", "categoriaProducto": "Herramientas Eléctricas"},
            {"nombreProducto": "Soldador eléctrico 200A", "descripcionProducto": "Máquina de soldar inverter", "stockProducto": 6, "precioProducto": 135.00, "imagenProducto": "imagenes/e7.png", "categoriaProducto": "Herramientas Eléctricas"},
            {"nombreProducto": "Pulidora angular 4.5\"", "descripcionProducto": "Pulidora 750W con disco", "stockProducto": 11, "precioProducto": 39.00, "imagenProducto": "imagenes/e8.png", "categoriaProducto": "Herramientas Eléctricas"},
            {"nombreProducto": "Cargador de baterías 12V", "descripcionProducto": "Cargador inteligente portátil", "stockProducto": 9, "precioProducto": 23.00, "imagenProducto": "imagenes/e9.png", "categoriaProducto": "Herramientas Eléctricas"},

            # === PINTURA ===
            {"nombreProducto": "Brocha multiusos 3\"", "descripcionProducto": "Brocha con mango de madera", "stockProducto": 50, "precioProducto": 1.89, "imagenProducto": "imagenes/p1.png", "categoriaProducto": "Pintura"},
            {"nombreProducto": "Rodillo antigota 9\"", "descripcionProducto": "Rodillo con mango ergonómico", "stockProducto": 40, "precioProducto": 2.76, "imagenProducto": "imagenes/p2.png", "categoriaProducto": "Pintura"},
            {"nombreProducto": "Pintura látex blanca 1 gl", "descripcionProducto": "Pintura de interiores lavable", "stockProducto": 30, "precioProducto": 13.99, "imagenProducto": "imagenes/p3.png", "categoriaProducto": "Pintura"},
            {"nombreProducto": "Esmalte sintético 1/4", "descripcionProducto": "Esmalte brillante color azul", "stockProducto": 18, "precioProducto": 4.20, "imagenProducto": "imagenes/p4.png", "categoriaProducto": "Pintura"},
            {"nombreProducto": "Removedor de pintura 1L", "descripcionProducto": "Removedor tipo gel rápido", "stockProducto": 12, "precioProducto": 6.95, "imagenProducto": "imagenes/p5.png", "categoriaProducto": "Pintura"},
            {"nombreProducto": "Cinta masking tape 2\"", "descripcionProducto": "Cinta para pintar sin bordes", "stockProducto": 60, "precioProducto": 1.10, "imagenProducto": "imagenes/p6.png", "categoriaProducto": "Pintura"},
            {"nombreProducto": "Lija para pared grano 120", "descripcionProducto": "Lija para preparación de muros", "stockProducto": 90, "precioProducto": 0.60, "imagenProducto": "imagenes/p7.png", "categoriaProducto": "Pintura"},
            {"nombreProducto": "Diluyente para esmalte 1L", "descripcionProducto": "Disolvente para pinturas sintéticas", "stockProducto": 20, "precioProducto": 3.80, "imagenProducto": "imagenes/p8.png", "categoriaProducto": "Pintura"},

            # === ILUMINACIÓN ===
            {"nombreProducto": "Foco LED SENSOR 9W", "descripcionProducto": "Foco con sensor de movimiento", "stockProducto": 60, "precioProducto": 2.48, "imagenProducto": "imagenes/l1.png", "categoriaProducto": "Iluminación"},
            {"nombreProducto": "Lámpara exterior doble", "descripcionProducto": "Luminaria negra con dos focos", "stockProducto": 12, "precioProducto": 17.58, "imagenProducto": "imagenes/l2.png", "categoriaProducto": "Iluminación"},
            {"nombreProducto": "Tubo LED T8 18W", "descripcionProducto": "Tubo LED 120cm luz blanca", "stockProducto": 30, "precioProducto": 4.25, "imagenProducto": "imagenes/l3.png", "categoriaProducto": "Iluminación"},
            {"nombreProducto": "Reflector LED 50W", "descripcionProducto": "Reflector exterior luz fría", "stockProducto": 22, "precioProducto": 11.90, "imagenProducto": "imagenes/l4.png", "categoriaProducto": "Iluminación"},
            {"nombreProducto": "Aplique interior empotrado", "descripcionProducto": "Luz LED decorativa de techo", "stockProducto": 18, "precioProducto": 9.40, "imagenProducto": "imagenes/l5.png", "categoriaProducto": "Iluminación"},
            {"nombreProducto": "Interruptor de pared doble", "descripcionProducto": "Interruptor clásico blanco", "stockProducto": 45, "precioProducto": 2.00, "imagenProducto": "imagenes/l6.png", "categoriaProducto": "Iluminación"},
            {"nombreProducto": "Toma corriente 2P+T", "descripcionProducto": "Toma de enchufe polarizado", "stockProducto": 38, "precioProducto": 1.75, "imagenProducto": "imagenes/l7.png", "categoriaProducto": "Iluminación"},
        ]

        for prod in productos:
            db.add(Producto(**prod))
        db.commit()
