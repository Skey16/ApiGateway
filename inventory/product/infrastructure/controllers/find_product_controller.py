from flask import Blueprint, request, jsonify
from product.application.usecases.find_product import BuscarProductoPorNombre

buscar_producto_por_nombre_blueprint = Blueprint('buscar_producto_por_nombre', __name__)

def inicializar_endpoint_buscar_producto_por_nombre(repositorio):
    buscar_producto_por_nombre_usecase = BuscarProductoPorNombre(repositorio_producto=repositorio)

    @buscar_producto_por_nombre_blueprint.route('/buscar', methods=['GET'])
    def buscar_producto_por_nombre():
        nombre = request.args.get('nombre', '')
        try:
            productos = buscar_producto_por_nombre_usecase.ejecutar(nombre)
            return jsonify(productos), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404  # Not Found
