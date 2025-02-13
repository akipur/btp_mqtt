import sys

import paho.mqtt.client as mqtt

class Publisher:
	def __init__():
		self.client = mqtt.Client()
		self.hostname = hostname
		self.port = port
		self.keep_alive = keep_alive

	def publish_message(topic = "", message = ""):
		try:
			self.client.publish(topic, message, 0)
		except:
			print("Error sending message to topic")

	def connect():
		try:
			self.client.connect(self.hostname, self.port, self.keep_alive)
		except:
			print("Error connecting")

	def disconnect():
		try:
			self.client.disconnect()
		except:
			print("Error disconnecting")
