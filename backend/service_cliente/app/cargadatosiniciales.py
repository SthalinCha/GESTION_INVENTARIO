from sqlalchemy.orm import Session
from models import Cliente

def cargar_clientes_iniciales(db: Session):
    if db.query(Cliente).count() == 0:
        clientes = [
            {"cedula": 1010101010, "nombreCliente": "Juan", "apellidoCliente": "Pérez", "correoCliente": "juan.perez@example.com", "telefonoCliente": "0991234561", "direccionCliente": "Av. Siempre Viva 123"},
            {"cedula": 2020202020, "nombreCliente": "Ana", "apellidoCliente": "Gómez", "correoCliente": "ana.gomez@example.com", "telefonoCliente": "0987654322", "direccionCliente": "Calle Falsa 456"},
            {"cedula": 3030303030, "nombreCliente": "Carlos", "apellidoCliente": "Ruiz", "correoCliente": "carlos.ruiz@example.com", "telefonoCliente": None, "direccionCliente": None},
            {"cedula": 4040404040, "nombreCliente": "María", "apellidoCliente": "López", "correoCliente": "maria.lopez@dominio.com", "telefonoCliente": "0971122333", "direccionCliente": "Jr. Miraflores 789"},
            {"cedula": 5050505050, "nombreCliente": "Pedro", "apellidoCliente": "Ramírez", "correoCliente": "pedro.ramirez@correo.org", "telefonoCliente": "0965544334", "direccionCliente": "Paseo de la Reforma 101"},
            {"cedula": 6060606060, "nombreCliente": "Laura", "apellidoCliente": "Torres", "correoCliente": "laura.torres@mail.net", "telefonoCliente": "0959988775", "direccionCliente": "Blvd. Los Olivos 202"},
            {"cedula": 7070707070, "nombreCliente": "Diego", "apellidoCliente": "Vargas", "correoCliente": "diego.vargas@web.com", "telefonoCliente": "0943322116", "direccionCliente": "Calle del Sol 303"},
            {"cedula": 8080808080, "nombreCliente": "Sofía", "apellidoCliente": "Castro", "correoCliente": "sofia.castro@inbox.com", "telefonoCliente": "0937766557", "direccionCliente": "Av. Libertador 404"},
            {"cedula": 9090909090, "nombreCliente": "Gabriel", "apellidoCliente": "Morales", "correoCliente": "gabriel.morales@mycorp.com", "telefonoCliente": "0921100988", "direccionCliente": "Carrera 5ta 505"},
            {"cedula": 1010101011, "nombreCliente": "Valeria", "apellidoCliente": "Silva", "correoCliente": "valeria.silva@company.org", "telefonoCliente": "0915544339", "direccionCliente": "Ronda de Segovia 606"},
            {"cedula": 1111111111, "nombreCliente": "Andrés", "apellidoCliente": "Mendoza", "correoCliente": "andres.mendoza@email.net", "telefonoCliente": "0909988710", "direccionCliente": "Plaza Mayor 707"},
            {"cedula": 1212121212, "nombreCliente": "Isabel", "apellidoCliente": "Núñez", "correoCliente": "isabel.nunez@provider.com", "telefonoCliente": "0990011211", "direccionCliente": "Calle Larga 808"},
            {"cedula": 1313131313, "nombreCliente": "Fernando", "apellidoCliente": "Rojas", "correoCliente": "fernando.rojas@service.com", "telefonoCliente": "0987766512", "direccionCliente": "Av. El Dorado 909"},
            {"cedula": 1414141414, "nombreCliente": "Jimena", "apellidoCliente": "León", "correoCliente": "jimena.leon@portal.org", "telefonoCliente": "0976655413", "direccionCliente": "Jr. La Unión 111"},
            {"cedula": 1515151515, "nombreCliente": "Martín", "apellidoCliente": "Salazar", "correoCliente": "martin.salazar@solution.com", "telefonoCliente": "0965544314", "direccionCliente": "Boulevard del Ejército 222"},
            {"cedula": 1616161616, "nombreCliente": "Camila", "apellidoCliente": "Guerrero", "correoCliente": "camila.guerrero@system.com", "telefonoCliente": "0954433215", "direccionCliente": "Calle 10ma 333"},
            {"cedula": 1717171717, "nombreCliente": "Daniela", "apellidoCliente": "Soto", "correoCliente": "daniela.soto@interface.com", "telefonoCliente": "0932211017", "direccionCliente": "Pasaje Central 555"},
            {"cedula": 1818181818, "nombreCliente": "Alejandro", "apellidoCliente": "Herrera", "correoCliente": "alejandro.herrera@tech.net", "telefonoCliente": "0921100918", "direccionCliente": "Ruta del Spondylus 666"},
            {"cedula": 1919191919, "nombreCliente": "Lucía", "apellidoCliente": "Ibáñez", "correoCliente": "lucia.ibanez@global.com", "telefonoCliente": "0910099819", "direccionCliente": "Av. De los Shyris 777"}
        ]
        for cliente in clientes:
            db.add(Cliente(**cliente))
        db.commit()
