from flask import Blueprint
from order.infrastructure.controllers.create_order_controller import orden_blueprint, inicializar_endpoint_orden
from order.infrastructure.controllers.list_order_controller import listar_orden_blueprint, inicializar_endpoint_listar_orden
from order.infrastructure.controllers.update_order_status_controller import actualizar_estado_orden_blueprint, inicializar_endpoint_actualizar_estado_orden
from order.infrastructure.repositories.order_repository import RepositorioOrdenMongoDB

orden_router = Blueprint('orden_router', __name__)

def inicializar_endpoints_orden():
    repositorio_orden = RepositorioOrdenMongoDB(cadena_conexion='mongodb://localhost:27017/', nombre_base_datos='orden')
    inicializar_endpoint_orden(repositorio_orden)
    inicializar_endpoint_listar_orden(repositorio_orden)
    inicializar_endpoint_actualizar_estado_orden(repositorio_orden)

inicializar_endpoints_orden()

orden_router.register_blueprint(orden_blueprint, url_prefix='/')
orden_router.register_blueprint(listar_orden_blueprint, url_prefix='/')
orden_router.register_blueprint(actualizar_estado_orden_blueprint, url_prefix='/')
