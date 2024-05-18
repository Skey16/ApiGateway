from flask import Blueprint, jsonify
from order.application.usecases.list_order import ListarOrdenes

listar_orden_blueprint = Blueprint('listar_orden', __name__)

def inicializar_endpoint_listar_orden(repositorio_orden):
    listar_ordenes_usecase = ListarOrdenes(repositorio_orden=repositorio_orden)

    @listar_orden_blueprint.route('', methods=['GET'])
    def listar_ordenes():
        try:
            ordenes = listar_ordenes_usecase.ejecutar()
            return jsonify(ordenes), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
