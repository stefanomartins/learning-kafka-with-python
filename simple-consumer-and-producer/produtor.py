from kafka import KafkaProducer as kp
import random
import time

produtor = kp(bootstrap_servers="192.168.64.2:9092")

i = 0
try:
    while True:
        n = random.random()
        produtor.send("mensagens", key=b"Mensagem %d" % i, value=b"Mensagem %f" % n)
        produtor.flush()
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print("Produtor encerrado.")
    produtor.close()