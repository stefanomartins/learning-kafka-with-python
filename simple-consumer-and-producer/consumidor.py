from kafka import KafkaConsumer as kc

consumidor = kc(
    "mensagens",
    bootstrap_servers="192.168.64.2:9092",
    consumer_timeout_ms=3000,
    group_id="consumidores",
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

try:
    while True:
        for mensagem in consumidor:
            print(f"Topic: {mensagem.topic}")
            print(f"Partição: {mensagem.partition}")
            print(f"Chave: {mensagem.key}")
            print(f"Offset: {mensagem.offset}")
            print(f"Mensagem: {mensagem.value.decode('utf-8')}")
            print("-" * 80)
except KeyboardInterrupt:
    print("Consumidor encerrado.")
    consumidor.close()