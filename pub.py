import paho.mqtt.client as paho
import sys

# Callback function on connection to broker


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print("Connection failed with code", rc)


publisher = paho.Client(paho.CallbackAPIVersion.VERSION2)  # create a publisher

if publisher.connect("localhost", 1883, 60) != 0:  # connect the publisher to the broker
    print("Could not connect to MQTT Broker\n")
    sys.exit(-1)
else:
    print("Connected to MQTT Broker\n")

msg = input("Enter the message you want to publish:\n")
publisher.publish("test/status", msg, 0)  # test/status is the msg topic

publisher.disconnect()
