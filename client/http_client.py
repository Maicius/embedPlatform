import serial
import requests
from time import sleep
from embed_nju.util.jedis import get_raw_data
from embed_nju.util.constant import RAW_DISTANCE_KEY, RAW_TEMPERATURE_KEY, RAW_LIGHT_KEY, RAW_WET_KEY

def send_packet_by_http(data):

    url = 'http://localhost:8000/'

    url = url + 'upload_distance?distance=' + data
    print("http:" + url)
    requests.get(url)



def send_simulate():
    while True:
        try:
            data = 'temperature:10'
            send_packet_by_http(data)
            data = 'distance:10'
            send_packet_by_http(data)
            data = 'light:10'
            send_packet_by_http(data)
            sleep(1)
        except BaseException as e:
            print('Http Client Error Begin========================')
            print(e)
            print('Http Client Error End========================')

def start_http_client():

    # send_simulate()
    print("Start http client----------------")
    while True:
        try:
            data = get_raw_data(RAW_DISTANCE_KEY)
            if data:
                send_packet_by_http(data)
            sleep(1)
        except:
            pass


if __name__ == '__main__':
    start_http_client()