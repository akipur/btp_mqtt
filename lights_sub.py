from mqtt_tools.subscriber import Subscriber 
from gpiozero import LED
import time

def on_connect(client, userdata, falgs, rc):
    print(f"Connected with result code {rc}")
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
subscribed_channel = Subscriber(message_handling = on_message)
subscribed_channel.subscribe_to("light_control")
subscribed_channel.connect()

