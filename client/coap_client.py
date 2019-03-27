from embed_nju.util.jedis import pop_raw_data
from embed_nju.util.constant import RAW_WET_KEY
from coapthon.client.helperclient import HelperClient
import time

host = "127.0.0.1"
port = 5683
path ="wet"

client = HelperClient(server=(host, port))
while True:
    payload=pop_raw_data(RAW_WET_KEY)
    if payload:
        response = client.post(path,payload)
        time.sleep(1)
    # print(response.pretty_print())
client.stop()
