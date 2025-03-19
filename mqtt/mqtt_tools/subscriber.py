import paho.mqtt.client as mqtt

class Subscriber:
    def __init__(self, hostname="mqtt.eclipseprojects.io", port=1883, keep_alive=60):
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.hostname = hostname
        self.port = port
        self.keep_alive = keep_alive

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe(self.topic)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode("utf-8")
        print(f"Received message: {msg.topic} {payload}")
    
    def connect(self, topic="test/topic"):
        self.topic = topic
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.hostname, self.port, self.keep_alive)
        print(f"Connected to broker at {self.hostname}:{self.port}")

        self.client.loop_forever()