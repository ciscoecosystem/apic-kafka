from kafka import KafkaConsumer
import json
from config import config

consumer = KafkaConsumer(
    config['system_id'] + '_sub',
     bootstrap_servers=[config['apic_host'] + ':9093'],
     security_protocol="SSL",
     ssl_check_hostname=False,
     ssl_cafile="cacert.crt",
     ssl_certfile="server.crt",
     ssl_keyfile="server.key",
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id=config['system_id'] + '_group',
     value_deserializer=lambda x: json.loads(x)
)

for message in consumer:
    print('Message: \n{}'.format(json.dumps(message.value, indent=4, sort_keys=True)))