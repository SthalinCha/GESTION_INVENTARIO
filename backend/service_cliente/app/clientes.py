from models import Usuario
import datetime

class Cliente(Usuario):
    def __init__(self, cedula: str, nombre: str, correo: str, direccion: str, fecha_registro: datetime.date, estado: str):
        super().__init__(cedula, nombre, correo, direccion, fecha_registro, estado)

    def realizar_compra(self):
        print(f"Cliente {self.nombre} está realizando una compra.")

# You can add client-specific service functions here if needed
def get_cliente_by_cedula(cedula: str):
    # This would typically interact with a database
    print(f"Buscando cliente con cédula: {cedula}")
    return None # Placeholder