import pika
import json
from pymongo import MongoClient
from bson import ObjectId

def disminuir_stock(canal, metodo, propiedades, cuerpo):
    print("Mensaje recibido")  # Mensaje de depuración al recibir el mensaje
    mensaje = json.loads(cuerpo)
    client = MongoClient('mongodb://localhost:27017/')
    db = client['inventario']
    coleccion_productos = db['productos']

    for producto in mensaje['productos']:
        id_producto = producto['id_producto']
        cantidad = producto['cantidad']
        resultado = coleccion_productos.update_one(
            {'_id': ObjectId(id_producto)},
            {'$inc': {'stock': -cantidad}}
        )
        print(f"Stock del producto {id_producto} actualizado, cantidad disminuida: {cantidad}")  # Mensaje de depuración para cada producto
    
    print(f"Stock actualizado para la orden {mensaje['id_orden']}")  # Mensaje de depuración al finalizar el procesamiento del mensaje
    canal.basic_ack(delivery_tag=metodo.delivery_tag)

credentials = pika.PlainCredentials('admin', 'admin*')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

try:
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='disminuir_stock', durable=False)  # Asegúrate de que la cola sea duradera

    channel.basic_consume(queue='disminuir_stock', on_message_callback=disminuir_stock)
    print('Esperando mensajes. Presiona Ctrl+C para salir')
    channel.start_consuming()
except Exception as e:
    print(f"Error al conectar o consumir mensajes: {e}")
