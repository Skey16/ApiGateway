class ActualizarEstadoOrden:
    def __init__(self, repositorio_orden):
        self.repositorio_orden = repositorio_orden

    def ejecutar(self, id_orden, nuevo_estado):
        return self.repositorio_orden.actualizar_estado(id_orden, nuevo_estado)
