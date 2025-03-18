from mqtt_tools.subscriber import Subscriber 
from gpiozero import LED
import time

class LED_control(Subscriber):
	def __init__(self):
		pass
	def take_action(msg):
    		print(f"Received message on topic {message.topic}: {message.payload}")
    		if msg == "ON":
        		led.on()
    		if msg == "OFF":
       			 led.off()

led = LED(18)
led.on()
subscriber = LED_Control()
subscriber.connect()
subscriber.subscribe("light_control")

