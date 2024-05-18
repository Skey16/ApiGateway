from flask import Blueprint, request, jsonify
from order.application.usecases.update_order_status import ActualizarEstadoOrden

actualizar_estado_orden_blueprint = Blueprint('actualizar_estado_orden', __name__)

def inicializar_endpoint_actualizar_estado_orden(repositorio_orden):
    actualizar_estado_orden_usecase = ActualizarEstadoOrden(repositorio_orden=repositorio_orden)

    @actualizar_estado_orden_blueprint.route('/actualizar_estado/<id_orden>', methods=['PUT'])
    def actualizar_estado_orden(id_orden):
        nuevo_estado = request.json.get('estado')
        if not nuevo_estado:
            return jsonify({"error": "Estatus es requerido"}), 400
        try:
            actualizar_estado_orden_usecase.ejecutar(id_orden, nuevo_estado)
            return jsonify({"mensaje": "Estatus actualizado exitosamente"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
