import pika
import json
from order.domain.entities.order import Orden

class ActualizarEstadoOrden:
    def __init__(self, repositorio_orden):
        self.repositorio_orden = repositorio_orden

    def ejecutar(self, id_orden, nuevo_estado):
        # Intentamos actualizar el estado de la orden.
        if not self.repositorio_orden.actualizar_estado(id_orden, nuevo_estado):
            raise ValueError("Orden no encontrada o estado no actualizado")

        # Recuperar la orden actualizada para poder trabajar con ella
        orden_actualizada = self.repositorio_orden.obtener_por_id(id_orden)
        if not orden_actualizada:
            raise ValueError("Orden no encontrada después de actualizar")

        # Verificar y manejar el nuevo estado
        if nuevo_estado == 'Enviado':
            self.publicar_mensaje_disminuir_stock(orden_actualizada)

def publicar_mensaje_disminuir_stock(self, orden):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        print("Conexión exitosa")
    except pika.exceptions.AMQPConnectionError as error:
        print(f"No se pudo conectar a RabbitMQ: {error}")
    channel = connection.channel()
    channel.queue_declare(queue='disminuir_stock')

    mensaje = {
        'id_orden': str(orden.id),
        'productos': [{'id_producto': p.id_producto, 'cantidad': p.cantidad} for p in orden.productos_orden]
    }

    channel.basic_publish(
        exchange='',
        routing_key='/disminuir_stock',
        body=json.dumps(mensaje)
    )
    print("Mensaje publicado a disminuir_stock")  # Añade esta línea

    connection.close()


