from flask import Blueprint
from product.infrastructure.controllers.create_product_controller import producto_blueprint, inicializar_endpoint_producto
from product.infrastructure.controllers.list_product_controller import listar_producto_blueprint, inicializar_endpoint_listar_producto
from product.infrastructure.controllers.delete_product_controller import eliminar_producto_blueprint, inicializar_endpoint_eliminar_producto
from product.infrastructure.controllers.find_product_controller import buscar_producto_por_nombre_blueprint, inicializar_endpoint_buscar_producto_por_nombre
from product.infrastructure.repositories.product_repository import RepositorioProductoMongoDB

producto_router = Blueprint('producto_router', __name__)

def inicializar_endpoints_producto(repositorio):
    inicializar_endpoint_producto(repositorio)
    inicializar_endpoint_listar_producto(repositorio)
    inicializar_endpoint_eliminar_producto(repositorio)
    inicializar_endpoint_buscar_producto_por_nombre(repositorio)

repositorio = RepositorioProductoMongoDB(cadena_conexion='mongodb://localhost:27017/', nombre_base_datos='inventario')
inicializar_endpoints_producto(repositorio)

producto_router.register_blueprint(producto_blueprint, url_prefix='/')
producto_router.register_blueprint(listar_producto_blueprint, url_prefix='/')
producto_router.register_blueprint(eliminar_producto_blueprint, url_prefix='/')
producto_router.register_blueprint(buscar_producto_por_nombre_blueprint, url_prefix='/')
