#!/usr/bin/env python


#dummy code to check mqtt working

import paho.mqtt.client as mqtt

def on_connect(client, userdata,flags,rc):
    print ("connected with result code" +str(rc))
    client.subscribe("outTopic/#")

def on_message(client,userdata,msg):
    print(msg.topic+" "+str(msg.payload))

client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message

#client.connect("iot.eclipse.org",1883,60)
#client.connect("127.0.0.1",1883,60)
client.connect("52.64.180.1",1883,60)

client.loop_forever()
