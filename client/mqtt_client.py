import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import redis


def start_mqtt_client():
    embed_distance = [{"time": "2019-03-22 14:47:18", "value": "76"}]
    embed_light = [{"time": "2019-03-22 14:47:18", "value": "76"}]
    embed_temperature = [{"time": "2019-03-22 14:47:18", "value": "76"}]
    embed_data = [{"name": "embed_distance", "time": "2019-03-22 14:47:18", "value": "72"},
                  {"name": "embed_light", "time": "2019-03-22 14:47:18", "value": "73"},
                  {"name": "embed_temperature", "time": "2019-03-22 14:47:18", "value": "74"}]
    
    while True:
        # print(json.dumps(embed_data))
        print("mqtt send success")
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
