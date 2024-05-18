from flask import Blueprint, request, jsonify
from product.application.usecases.delete_product import EliminarProducto

eliminar_producto_blueprint = Blueprint('eliminar_producto', __name__)

def inicializar_endpoint_eliminar_producto(repositorio):
    eliminar_producto_usecase = EliminarProducto(repositorio_producto=repositorio)

    @eliminar_producto_blueprint.route('/<id_producto>', methods=['DELETE'])
    def eliminar_producto(id_producto):
        try:
            eliminar_producto_usecase.ejecutar(id_producto)
            return jsonify({"mensaje": "Producto eliminado exitosamente"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
