import paho.mqtt.client as mqtt
import json
import redis
from .util.jedis import get_pool
from .util.constant import DISTANCE_KEY,TEMPERATURE_KEY, LIGHT_KEY

data=[{}]
def pre_process_data(time_str,data, key):
    conn = redis.Redis(connection_pool=get_pool())
    distance_dict = json.dumps(dict(time=time_str, value=data))
    conn.rpush(key, str(distance_dict))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # 在这里处理业务逻辑
    data=json.loads(msg.payload)
    print(data)
    if (data is not None):
        b1 = data[0].get("time")
        b2 = data[1].get("time")
        b3 = data[2].get("time")
        c1=data[0].get("value")
        c2=data[1].get("value")
        c3=data[2].get("value")
        pre_process_data(b1, c1, DISTANCE_KEY)
        pre_process_data(b2, c2, LIGHT_KEY)
        pre_process_data(b3, c3, TEMPERATURE_KEY)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.subscribe("paho/temperature")
client.loop_forever()