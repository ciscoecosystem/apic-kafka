# Kafka Cisco APIC Object Subscription

The Cisco APIC controller provide a Kafka bus to allow subscription to object creation, modification or deletion events. This repo shows how to generate certificates to access the Kafka bus and how to add classes to the Kafka topic.

## Requirements
APIC v4.2 or newer
Python

## Install
Python must be installed (Following documentation has been tested with Python3)
We recommend you use a dedicated virtual environment.

The following install the requirements and generate the meta file used by PyACI.
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
rmetagen.py -u admin YOUR_APIC_IP_ADDRESS
```

To connect to the Kafka bus, you will need to allow port TCP/9093 to be opened in the APIC firewall.
This is done by configuring a OOB Contract. See some example of how to configure an OOB contract here: https://unofficialaciguide.com/2018/04/13/changing-the-default-port-for-https-access-to-the-apic-gui/

## Use
Edit the config.py to point to your APIC controller using the proper credentials. 
Also specify the System ID which is the ID used to reference to your Kafka Consumer and the certificates and topic created for it.
It can be any string that is unique enough.
Also specify the classes you want to register to be notified about in the classes list in the config.

You can use the gen_kafka_cert.py to generate the proper certificate files to use to connect to the APIC Kafka bus.
```
python gen_kafka_cert.py
```

You can use the subscription.py to create the aaaKafkaSubscription and aaaKafkaSubscriptionClass MOs which identify the Topic to be created, which System ID it is created for and what classes are monitored by this topic.
The Kafka topic name is your System ID with the "_sub" suffix so in our example it is "MySuperSystemID_sub".
```
python subscription.py
```

You can use the consumer.py to connect and print the messages on the Kafka topic you created.
```
python consumer.py
```