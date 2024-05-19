import pika
import json
from order.domain.entities.order import Orden

class ActualizarEstadoOrden:
    def __init__(self, repositorio_orden):
        self.repositorio_orden = repositorio_orden

    def ejecutar(self, id_orden, nuevo_estado):
        if not self.repositorio_orden.actualizar_estado(id_orden, nuevo_estado):
            raise ValueError("Orden no encontrada o estado no actualizado")

        orden_actualizada = self.repositorio_orden.obtener_por_id(id_orden)
        if not orden_actualizada:
            raise ValueError("Orden no encontrada después de actualizar")

        if nuevo_estado.lower() == 'enviado':
            self.publicar_mensaje_disminuir_stock(orden_actualizada)

    def publicar_mensaje_disminuir_stock(self, orden):
        connection = None
        try:
                        # Depuración: Imprimir la estructura del diccionario orden
            print("Estructura de orden recibida:", orden)

            credentials = pika.PlainCredentials('admin', 'admin*')
            parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            channel.queue_declare(queue='disminuir_stock', durable=False)

            # Asegúrate de que el diccionario orden contiene las claves esperadas
            if '_id' not in orden or 'productos_orden' not in orden:
                raise ValueError("El diccionario orden no contiene las claves necesarias")

            credentials = pika.PlainCredentials('admin', 'admin*')
            parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
            connection = pika.BlockingConnection(parameters)
            channel = connection.channel()
            channel.queue_declare(queue='disminuir_stock', durable=False)

            mensaje = {
                'id_orden': str(orden['_id']),  # Cambiado a '_id'
                'productos': [
                    {
                        'id_producto': p['id_producto'],
                        'cantidad': p['cantidad']
                    } for p in orden['productos_orden']
                ]
            }
            channel.basic_publish(
                exchange='',
                routing_key='disminuir_stock',
                body=json.dumps(mensaje),
                properties=pika.BasicProperties(delivery_mode=2)
            )
            print("Mensaje publicado a disminuir_stock")
        except pika.exceptions.AMQPConnectionError as e:
            print(f"Error de conexión a RabbitMQ: {e}")
        except pika.exceptions.AMQPChannelError as e:
            print(f"Error de canal en RabbitMQ: {e}")
        except Exception as e:
            print(f"Error general: {e}")
        finally:
            if connection and connection.is_open:
                connection.close()
