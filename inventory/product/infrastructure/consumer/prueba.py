from gc import callbacks
import pika

def consumir_mensajes():
    credentials = pika.PlainCredentials('admin', 'admin*')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='disminuir_stock', durable=True)
    channel.basic_consume(queue='disminuir_stock', on_message_callback=callbacks, auto_ack=True)

    print(' [*] Esperando mensajes. Para salir presiona CTRL+C')
    channel.start_consuming()
