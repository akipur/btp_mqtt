from mqtt_tools.publisher import Publisher

mqtt_channel = "test/topic"

publisher = Publisher(hostname="mqtt.eclipseprojects.io", port=1883, keep_alive=60)
publisher.connect()

while True:
    msg = input("Enter 'ON' or 'OFF' to control the LED: ").strip().upper()
    if msg in ["ON", "OFF"]:
        publisher.publish_message(mqtt_channel, msg)
        print(f"Sent: {msg}")
    else:
        print("Invalid input. Enter 'ON' or 'OFF'.")