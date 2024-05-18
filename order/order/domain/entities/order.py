from datetime import datetime

class Orden:
    def __init__(self, total, estado, productos_orden=[]):
        self.total = total
        self.fecha = datetime.now()
        self.estado = estado
        self.productos_orden = productos_orden
