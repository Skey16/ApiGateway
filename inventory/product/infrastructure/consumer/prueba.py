import pika
import sys

def main():
    # Configura tus credenciales y dirección del servidor aquí
    credentials = pika.PlainCredentials('admin', 'admin*')
    parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

    # Intenta establecer la conexión
    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        print("Conexión exitosa")
    except Exception as e:
        print(f"Error al conectar a RabbitMQ: {e}")
        sys.exit(1)

    # Declarar una cola
    queue_name = 'test_queue'
    channel.queue_declare(queue=queue_name, durable=True)

    # Publicar un mensaje
    message = "Hola RabbitMQ!"
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message)
    print(f"Mensaje enviado: {message}")

    # Configurar una función de callback para cuando se reciba un mensaje
    def callback(ch, method, properties, body):
        print(f"Mensaje recibido: {body.decode()}")
        # Asegúrate de reconocer el mensaje
        ch.basic_ack(delivery_tag=method.delivery_tag)
        connection.close()

    # Consumir el mensaje
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=False)
    print('Esperando mensajes. Para salir presiona CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    main()
