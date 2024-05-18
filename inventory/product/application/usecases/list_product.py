class ListarProductos:
    def __init__(self, repositorio_producto):
        self.repositorio_producto = repositorio_producto

    def ejecutar(self):
        productos = self.repositorio_producto.encontrar_todos()
        if not productos:
            raise ValueError("No hay productos disponibles")
        return productos
