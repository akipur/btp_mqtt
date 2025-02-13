import sys

import paho.mqtt.client as mqtt

class Publisher:
	def __init__(self, hostname = "localhost", port = 1833, keep_alive = 60):
		self.client = mqtt.Client()
		self.hostname = hostname
		self.port = port
		self.keep_alive = keep_alive

	def publish_message(self, topic = "", message = ""):
		try:
			self.client.publish(topic, message, 0)
		except:
			print("Error sending message to topic")

	def connect(self):
		try:
			self.client.connect(self.hostname, self.port, self.keep_alive)
		except:
			print("Error connecting")

	def disconnect(self):
		try:
			self.client.disconnect()
		except:
			print("Error disconnecting")
