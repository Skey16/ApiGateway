from flask import Blueprint, jsonify
from product.application.usecases.list_product import ListarProductos

listar_producto_blueprint = Blueprint('listar_producto', __name__)

def inicializar_endpoint_listar_producto(repositorio):
    listar_productos_usecase = ListarProductos(repositorio_producto=repositorio)

    @listar_producto_blueprint.route('', methods=['GET'])
    def listar_productos():
        try:
            productos = listar_productos_usecase.ejecutar()
            return jsonify(productos), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
