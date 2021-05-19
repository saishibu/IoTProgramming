import paho.mqtt.client as mqtt

#Define MQTT Broker address and Port
broker="localhost"
port="1883"

#Create a variable to store your message
payload="Hello from MQTT"

#Create a variable for MQTT Topic
topic = "mqtt/gcp"

#Create a client
client = mqtt.Client()

#Connect client to MQTT Broker
client.connect(broker,port,0)

#Publish message to the client
(rc,mid)=client.publish(topic,payload);

#Disconnect from the client
client.disconnect();
