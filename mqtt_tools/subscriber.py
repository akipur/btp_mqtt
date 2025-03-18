import sys

import paho.mqtt.client as mqtt

class Subscriber:
	def __init__(self, hostname = "mqtt.eclipseprojects.io", port = 1883, keep_alive = 60):
		self.client = mqtt.Client(callback_api_version = mqtt.CallbackAPIVersion.VERSION2)
		self.hostname = hostname
		self.port = port
		self.keep_alive = keep_alive
		self.topics = set()

	def subscribe_to(self, topic = ""):
		self.topics.add(topic)
		self.client.subscribe(topic)

	def unsubscribe(self, topic = None):
		if not topic:
			for topic in topics:
				self.client.unsubscribe(topic)
			self.topics = set()
		else:
			self.client.unsubscribe(topic)
			self.topics.remove(topic)

	def on_connect(self, client, userdata, flags, reason_code, properties):
		print(f"Connected with result code {reason_code}")
		for topic in topics:
			self.client.subscribe(topic) 

	def on_message(self, client, userdata, message):
		payload = message.payload.decode("utf-8")
		print(f"Received Message: {message.topic} {payload}")
		take_action(payload)

	def take_action(payload):
		pass

	def connect(self):
		try:
			self.client.on_connect = self.on_connect
			self.client.on_message = self.on_message
			self.client.connect(self.hostname, self.port, self.keep_alive)
			print(f"Connected to broker at {self.hostname}:{self.port}")
			self.client.loop_forever()
		except:
			print("Unable to connect to host")

	def disconnect(self):
		try:
			self.client.disconnect()
		except:
			print("Ran into an error while disconnecting")
