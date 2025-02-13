import sys

import paho.mqtt.client as mqtt

class Subscriber:
	def __init__(self, hostname = "localhost", port = 1883, keep_alive = 60):
		self.client = mqtt.Client()
		self.hostname = hostname
		self.port = port
		self.keep_alive = keep_alive

	def subscribe_to(self, topic = ""):
		self.client.subscribe(topic)

	def connect(self):
		try:
			self.client.connect(self.hostname, self.port, self.keep_alive)
			self.client.loop_forever()
		except:
			print("Unable to connect to host")

	def disconnect(self):
		try:
			self.client.disconnect()
		except:
			print("Ran into an error while disconnecting")
