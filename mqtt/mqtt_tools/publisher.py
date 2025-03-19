import paho.mqtt.client as mqtt

class Publisher:
    def __init__(self, hostname="mqtt.eclipseprojects.io", port=1883, keep_alive=60):
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.hostname = hostname
        self.port = port
        self.keep_alive = keep_alive

    def publish_message(self, topic="test/topic", message="Hello"):
        self.client.publish(topic, message, qos=0)
        print(f"Published message: {message} to topic: {topic}")

    def connect(self):
        self.client.connect(self.hostname, self.port, self.keep_alive)
        print(f"Connected to broker at {self.hostname}:{self.port}")