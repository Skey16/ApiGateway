from flask import Blueprint, request, jsonify
from product.application.usecases.create_product import CrearProducto

producto_blueprint = Blueprint('producto', __name__)

def inicializar_endpoint_producto(repositorio):
    crear_producto_usecase = CrearProducto(repositorio_producto=repositorio)

    @producto_blueprint.route('', methods=['POST'])
    def crear_producto():
        datos = request.get_json()
        try:
            crear_producto_usecase.ejecutar(datos['nombre'], datos['precio'], datos['stock'])
            return jsonify({"mensaje": "Producto creado exitosamente"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 409 
        except Exception as e:
            return jsonify({"error": str(e)}), 400
