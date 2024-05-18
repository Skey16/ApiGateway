from flask import Blueprint, request, jsonify
from order.application.usecases.create_order import CrearOrden
from order.infrastructure.repositories.order_repository import RepositorioOrdenMongoDB

orden_blueprint = Blueprint('orden', __name__)

def inicializar_endpoint_orden(repositorio_orden):
    crear_orden_usecase = CrearOrden(repositorio_orden)

    @orden_blueprint.route('', methods=['POST'])
    def crear_orden():
        datos = request.get_json()
        try:
            crear_orden_usecase.ejecutar(datos['nombres_productos'], datos['cantidades'])
            return jsonify({"mensaje": "Orden creada exitosamente"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400
