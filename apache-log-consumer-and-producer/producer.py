import time
import re
import datetime
from kafka import KafkaProducer as kp

regexp = '^([\\d.]+) (\\S+) (\\S+) \\[([\\w:/]+\\s[+-]\\d{4})\\] \"(.+?)\" (\\d{3}) (\\d+) \"([^\"]+)\" \"(.+?)\"'
produtor = kp(bootstrap_servers='192.168.64.2:9092')

with open('/var/log/apache2/access.log', 'r') as my_file:
    while True:
        for linha in my_file:
            x = re.match(regexp, linha).groups()
            msg = bytes(str(x), encoding='utf-8')
            produtor.send('apachelog', msg)
            produtor.flush()
            print(f'Mensagem enviada em {datetime.datetime.now()}')