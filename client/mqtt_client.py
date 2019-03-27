import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import redis
from embed_nju.util.jedis import get_pool,pop_raw_data
from embed_nju.util.constant import RAW_TEMPERATURE_KEY

def start_mqtt_client():
    # embed_distance = [{"time": "2019-03-22 14:47:18", "value": "76"}]
    # embed_light = [{"time": "2019-03-22 14:47:18", "value": "76"}]
    # embed_temperature = [{"time": "2019-03-22 14:47:18", "value": "76"}]

    while True:
        data = pop_raw_data(RAW_TEMPERATURE_KEY)
        embed_data = {"name": "embed_temperature", "value": data}
        print("mqtt send success---------------------")
        if data is not None:
            publish.single("paho/temperature",
                           # payload="this is message:%s" %idx,
                           payload=json.dumps(embed_data),
                           hostname="iot.eclipse.org",
                           client_id="lora1",
                           # qos = 0,
                           # tls=tls,
                           port=1883,
                           protocol=mqtt.MQTTv311)

if __name__ == '__main__':
    start_mqtt_client()
