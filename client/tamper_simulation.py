import paho.mqtt.client as mqtt
import time

# -------------------------------------------------------
# This script simulates a tampered message sent over TLS.
# The subscriber should detect the incorrect HMAC.
# -------------------------------------------------------

fake_msg = "Temperature is 100°C||WRONGHASH123"

# MQTT Broker settings
BROKER = "localhost"
PORT = 8883  # Use secure port
TOPIC = "secure/topic"
USERNAME = "subin"
PASSWORD = "subin123"
CA_CERT_PATH = "C:/Users/subin/OneDrive/Desktop(1)/MQTT_Security_Project/broker_config/ca.crt"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("📶 Connected to broker securely.")
    else:
        print(f"❌ Connection failed with code {rc}")

if __name__ == "__main__":
    client = mqtt.Client(client_id="tamperclient")
    client.username_pw_set(USERNAME, PASSWORD)
    client.tls_set(ca_certs=CA_CERT_PATH)  # Secure TLS connection
    client.on_connect = on_connect

    client.connect(BROKER, PORT, 60)
    client.loop_start()
    time.sleep(0.2)

    result = client.publish(TOPIC, fake_msg)
    result.wait_for_publish()

    if result.rc == 0:
        print(f"❌ Tampered message sent: {fake_msg}")
    else:
        print("❌ Failed to publish tampered message.")

    client.loop_stop()
    client.disconnect()
