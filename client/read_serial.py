import serial
import redis

from embed_nju.util.constant import RAW_DISTANCE_KEY, RAW_TEMPERATURE_KEY, RAW_LIGHT_KEY, RAW_WET_KEY
from embed_nju.util.jedis import get_pool, push_raw_data, set_raw_data
import time

def read_serial():
    with serial.Serial('/dev/cu.usbmodem1411', 9600) as ser:
        while True:
            try:
                data = ser.readline().decode().strip()
                if data:
                    print("serial data begin:============")
                    print(data)
                    print("serial data end:============")
                    save_raw_to_redis(data)
            except:
                print("no data")



def save_raw_to_redis(data):
    data = data.split(':')
    data_type = data[0]
    data_value = data[1]
    if data_type == 'temperature':
        push_raw_data(data_value, RAW_TEMPERATURE_KEY)
    elif data_type == 'distance':
        set_raw_data(data_value, RAW_DISTANCE_KEY)
    elif data_type == 'light':
        set_raw_data(data_value, RAW_LIGHT_KEY)
    elif data_type == 'wet':
        push_raw_data(data_value, RAW_WET_KEY)

if __name__ == '__main__':
    read_serial()
