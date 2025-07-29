import datetime

class Usuario:
    def __init__(self, cedula: str, nombre: str, correo: str, direccion: str, fecha_registro: datetime.date, estado: str):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.fecha_registro = fecha_registro
        self.estado = estado

class Empleado(Usuario):
    def __init__(self, cedula: str, nombre: str, correo: str, direccion: str, fecha_registro: datetime.date, estado: str, cargo: str):
        super().__init__(cedula, nombre, correo, direccion, fecha_registro, estado)
        self.cargo = cargo

    def registrar_producto(self, producto):
        print(f"Empleado {self.nombre} está registrando el producto: {producto.nombre}")

    def registrar_factura(self, factura):
        print(f"Empleado {self.nombre} está registrando la factura: {factura.numero_factura}")

    def registrar_cliente(self, cliente):
        print(f"Empleado {self.nombre} está registrando al cliente: {cliente.nombre}")

    def gestionar_inventario(self):
        print(f"Empleado {self.nombre} está gestionando el inventario.")

class ImagenProducto:
    def __init__(self, ruta_archivo: str, tipo: str, tamano_kb: float):
        self.ruta_archivo = ruta_archivo
        self.tipo = tipo
        self.tamano_kb = tamano_kb

    def eliminar(self):
        print(f"Eliminando imagen: {self.ruta_archivo}")

    def mostrar(self):
        print(f"Mostrando imagen: {self.ruta_archivo}")