from pymongo import MongoClient
from bson import ObjectId
from order.domain.entities.order import Orden

class RepositorioOrdenMongoDB:
    def __init__(self, cadena_conexion, nombre_base_datos):
        self.cliente = MongoClient(cadena_conexion)
        self.db = self.cliente[nombre_base_datos]
        self.coleccion_ordenes = self.db['orden']

    def guardar(self, orden: Orden):
        datos_orden = {
            "total": orden.total,
            "fecha": orden.fecha,
            "estado": orden.estado,
            "productos_orden": [{"id_producto": p.id_producto, "precio": p.precio, "cantidad": p.cantidad} for p in orden.productos_orden]
        }
        self.coleccion_ordenes.insert_one(datos_orden)

    def encontrar_todas(self):
        ordenes = list(self.coleccion_ordenes.find({}))
        if not ordenes:
            raise ValueError("No existen ordenes")
        # Convertir ObjectId a string
        return [{
            "_id": str(orden["_id"]),
            "total": orden["total"],
            "fecha": orden["fecha"],
            "estado": orden["estado"],
            "productos_orden": [{"id_producto": str(p["id_producto"]), "precio": p["precio"], "cantidad": p["cantidad"]} for p in orden["productos_orden"]]
        } for orden in ordenes]

    def actualizar_estado(self, id_orden, nuevo_estado):
        resultado = self.coleccion_ordenes.update_one(
            {"_id": ObjectId(id_orden)},
            {"$set": {"estado": nuevo_estado}}
        )
        if resultado.matched_count == 0:
            raise ValueError("Orden no encontrada")
        if resultado.modified_count == 0:
            raise ValueError("El estatus no fue actualizado")
        return True
