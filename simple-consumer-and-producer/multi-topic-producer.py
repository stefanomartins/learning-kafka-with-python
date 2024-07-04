from kafka import KafkaProducer as kp
import random
import time

produtor = kp(bootstrap_servers="localhost:29092")

try:
    i = 0
    while True:
        n = random.random()
        produtor.send("mensagem-00", key=b"Mensagem %d" % i, value=b"Mensagem topico mensagem-00: %f" % n)
        produtor.send("mensagem-01", key=b"Mensagem %d" % i, value=b"Mensagem topico mensagem-01: %f" % n)
        produtor.flush()
        time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print("Produtor encerrado")
    produtor.close()