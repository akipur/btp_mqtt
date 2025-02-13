import sys

import paho.mqtt.client as mqtt

class Subscriber:
	def __init__(hostname = "localhost", port = 1883, keep_alive = 60, message_handling = None):
		self.client = mqtt.Client()
		self.hostname = hostname
		self.port = port
		self.keep_alive = keep_alive
		self.client.on_message = message_handling

	def subscribe_to(topic = ""):
		self.client.subscribe(topic)

	def connect():
		try:
			self.client.connect(self.hostname, self.port, self.keep_alive)
			self.client.loop_forever()
		except:
			print("Unable to connect to host")

	def disconnect():
		try:
			self.client.disconnect()
		except:
			print("Ran into an error while disconnecting")
