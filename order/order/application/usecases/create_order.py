import requests
from order.domain.entities.order import Orden
from order.domain.entities.order_product import ProductoOrden
from order.domain.validations.order_validations import validar_orden

class CrearOrden:
    def __init__(self, repositorio_orden):
        self.repositorio_orden = repositorio_orden

    def ejecutar(self, nombres_productos, cantidades):
        url_inventario = "http://localhost:8080/api/productos/buscar"  # URL actualizada

        productos_orden = []
        total = 0
        for nombre, cantidad in zip(nombres_productos, cantidades):
            response = requests.get(url_inventario, params={"nombre": nombre})  # Asegúrate de que los parámetros son correctos
            if response.status_code == 200 and response.json():
                datos_producto = response.json()[0]  # Asumiendo que la respuesta es una lista
                producto_orden = ProductoOrden(datos_producto["_id"], datos_producto["precio"], cantidad)
                productos_orden.append(producto_orden)
                total += datos_producto["precio"] * cantidad
            else:
                # Imprime la respuesta del servidor para depuración
                print(f"Error al obtener el producto: {response.status_code} - {response.text}")
                raise Exception(f"Producto {nombre} no encontrado en el inventario")

        orden = Orden(total=total, estado="Creado", productos_orden=productos_orden)
        validar_orden(orden)
        self.repositorio_orden.guardar(orden)
