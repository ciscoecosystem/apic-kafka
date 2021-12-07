from pyaci import Node
from config import config

apic = Node('https://' + config['apic_host'])
apic.methods.Login(config['apic_login']['username'], config['apic_login']['password']).POST()

mit = apic.mit
uni = mit.polUni()
subscription = uni.aaaUserEp().aaaKafkaEp().aaaKafkaSubscription(subID='subid_pythontest', subscriberCN=config['system_id'])

for class_name in config['classes']:
    subscription.aaaKafkaSubscriptionClass(subscriptionClass=class_name)

subscription.DELETE()
subscription.POST()
print(subscription.Json)