class EliminarProducto:
    def __init__(self, repositorio_producto):
        self.repositorio_producto = repositorio_producto

    def ejecutar(self, id_producto):
        self.repositorio_producto.eliminar_por_id(id_producto)
