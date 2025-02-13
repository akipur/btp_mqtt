from mqtt_tools.subscriber import Subscriber 
from gpiozero import LED
import time

def on_connect(client, userdata, flags, rc):
	print(f"Connected with {rc}")
	client.subscribe("light_control")

def on_message(client, userdata, message): 
    msg = message.payload.decode("utf-8").strip()
    print(f"Received message on topic {message.topic}: {message.payload}")
    if msg == "ON":
        led.on()
    if msg == "OFF":
        led.off()

led = LED(18)
led.on()
subscribed_channel = Subscriber()
subscribed_channel.client.on_message = on_message
subscribed_channel.client.on_connect = on_connect
subscribed_channel.connect()

