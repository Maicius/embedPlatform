import paho.mqtt.client as mqtt
import json
import redis
from embed_nju.util.jedis import get_pool
from embed_nju.util.constant import DISTANCE_KEY,TEMPERATURE_KEY, LIGHT_KEY

class MqttServer(object):
    def __init__(self):
        self.data = [{}]

    def pre_process_data(self, time_str, data, key):
        conn = redis.Redis(connection_pool=get_pool())
        distance_dict = json.dumps(dict(time=time_str, value=data))
        conn.rpush(key, str(distance_dict))

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        # 在这里处理业务逻辑
        data = json.loads(msg.payload)
        print("mqtt Server:", data)
        if (data is not None):
            b1 = data[0].get("time")
            b2 = data[1].get("time")
            b3 = data[2].get("time")
            c1 = data[0].get("value")
            c2 = data[1].get("value")
            c3 = data[2].get("value")
            self.pre_process_data(b1, c1, DISTANCE_KEY)
            self.pre_process_data(b2, c2, LIGHT_KEY)
            self.pre_process_data(b3, c3, TEMPERATURE_KEY)

def start_mqtt_server():
    server = MqttServer()
    client = mqtt.Client()
    client.on_connect = server.on_connect
    client.on_message = server.on_message
    client.connect("iot.eclipse.org", 1883, 60)
    client.subscribe("paho/temperature")
    client.loop_forever()

if __name__ == '__main__':
    start_mqtt_server()