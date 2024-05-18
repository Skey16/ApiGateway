class ListarOrdenes:
    def __init__(self, repositorio_orden):
        self.repositorio_orden = repositorio_orden

    def ejecutar(self):
        return self.repositorio_orden.encontrar_todas()
