from pymongo import MongoClient
from bson import ObjectId
from product.domain.entities.product import Producto

class RepositorioProductoMongoDB:
    def __init__(self, cadena_conexion, nombre_base_datos):
        self.cliente = MongoClient(cadena_conexion)
        self.db = self.cliente[nombre_base_datos]
        self.coleccion_productos = self.db['producto']
    
    def buscar_por_nombre(self, nombre):
        productos = list(self.coleccion_productos.find({"nombre": {"$regex": nombre, "$options": "i"}}))
        if not productos:
            raise ValueError("No se encontraron productos con ese nombre")
        # Convertir ObjectId a string
        return [{**producto, "_id": str(producto["_id"])} for producto in productos]

    def guardar(self, producto: Producto):
        try:
            producto_existente = self.buscar_por_nombre(producto.nombre)
            if producto_existente:
                raise ValueError("Producto ya existente")
        except ValueError as e:
            if str(e) == "No se encontraron productos con ese nombre":
                pass  # Este caso está bien, podemos proceder a guardar
            else:
                raise
        datos_producto = producto.__dict__
        self.coleccion_productos.insert_one(datos_producto)

    def encontrar_todos(self):
        productos = self.coleccion_productos.find({})
        return [{**producto, "_id": str(producto["_id"])} for producto in productos]
    
    def eliminar_por_id(self, id_producto):
        resultado = self.coleccion_productos.delete_one({"_id": ObjectId(id_producto)})
        if resultado.deleted_count == 0:
            raise ValueError("Producto no encontrado")
