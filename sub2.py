import paho.mqtt.client as paho
import sys

# Callback function on connection to broker


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print("Connection failed with code", rc)


def onMessage(client, userdata, msg):
    print(msg.topic + ":" + msg.payload.decode())


client = paho.Client(paho.CallbackAPIVersion.VERSION2)
client.on_message = onMessage

if client.connect("localhost", 1883, 60) != 0:
    print("Could not connect to MQTT Broker\n")
    sys.exit(-1)
else:
    print("Connected to MQTT Broker\n")

sub=input("Enter the topic you want to subscribe to:\n")
client.subscribe("test/status")
client.subscribe("test/status/new")

try:
    print("Press Ctrl+C to exit\n")
    client.loop_forever()
except:
    print("Disconnecting from Broker\n")

client.disconnect()
