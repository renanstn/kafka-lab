from confluent_kafka import Consumer


consumer = Consumer(
    {
        "bootstrap.servers": "kafka:29092",
        "group.id": "mygroup",
        "auto.offset.reset": "earliest",
    }
)

consumer.subscribe(["mytopic"])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print("Received message: {}".format(msg.value().decode("utf-8")))

c.close()
