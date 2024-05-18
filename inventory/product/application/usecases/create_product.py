from product.domain.entities.product import Producto
from product.domain.validations.product_validations import validar_producto

class CrearProducto:
    def __init__(self, repositorio_producto):
        self.repositorio_producto = repositorio_producto

    def ejecutar(self, nombre, precio, stock):
        producto = Producto(nombre, precio, stock)
        validar_producto(producto)
        self.repositorio_producto.guardar(producto)
