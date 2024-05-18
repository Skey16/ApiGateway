class BuscarProductoPorNombre:
    def __init__(self, repositorio_producto):
        self.repositorio_producto = repositorio_producto

    def ejecutar(self, nombre):
        return self.repositorio_producto.buscar_por_nombre(nombre)
