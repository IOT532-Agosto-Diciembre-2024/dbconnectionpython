import time

from database_manager import DatabaseManager
import paho.mqtt.client as mqtt
import keyboard

db_manager = DatabaseManager('localhost', 'ecommerce_532', 'root', 'andrestorres')


def on_message(client, userdata, msg):

    print(f"Mensaje recibido {msg.payload.decode()} {msg.topic}")


unacked_publish = set()
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

mqtt_client.on_message = on_message

mqtt_client.connect("broker.hivemq.com",1883)
mqtt_client.loop_start()
mqtt_client.subscribe("weccat/ultrasonido")

try:
    print("Esperando mensajes")
    while True:
        time.sleep(1)
except:
    print(f"Ocurrio un error")
finally:
    mqtt_client.loop_stop()
    mqtt_client.disconnect()





