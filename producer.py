import pika, json

params = pika.URLParameters('amqps://pjxegafa:lXMA-15j-OWVrBDtJES_68lAT3T07soD@baboon.rmq.cloudamqp.com/pjxegafa')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)