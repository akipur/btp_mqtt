from mqtt_tools.subscriber import Subscriber

subscriber = Subscriber(hostname="mqtt.eclipseprojects.io", port=1883, keep_alive=60)
subscriber.connect(topic="test/topic")
