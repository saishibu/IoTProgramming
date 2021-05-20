import paho.mqtt.client as mqtt
	
	broker="localhost"
	port=1883
	topic = "mqtt/gcp"
	
	client = mqtt.Client()
	client.connect(broker,port,0)
	client.subscribe(topic)
	client.on_message = on_message
	client.loop_forever()
  
  def on_message(client, userdata, msg):
	  payload=msg
    print(payload)
    client.disconnect()
