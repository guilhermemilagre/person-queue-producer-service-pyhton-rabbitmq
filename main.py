#!/usr/bin/env python
import json

import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='person', durable="true")

for i in range(0, 10000000):
    item = dict(id=str(i), name="User" + str(i))

    channel.basic_publish(exchange='personExchange',
                          routing_key='',
                          body=json.dumps(item))

    print(" [x] Sent 'User' messageId: " + str(i))

connection.close()
