import serial
import redis

from embed_nju.util.constant import RAW_DISTANCE_KEY, RAW_TEMPERATURE_KEY, RAW_LIGHT_KEY
from embed_nju.util.jedis import get_pool, push_raw_data


def read_serial():
    with serial.Serial('/dev/tty', 9600) as ser:
        while True:
            data = ser.readline().decode()
            if data is not None:
                save_raw_to_redis(data)


def save_raw_to_redis(data):
    data = data.split(':')
    data_type = data[0]
    data_value = data[1]
    if data_type == 'temperature':
        push_raw_data(data_value, RAW_TEMPERATURE_KEY)
    elif data_type == 'distance':
        push_raw_data(data_value, RAW_DISTANCE_KEY)
    elif data_type == 'light':
        push_raw_data(data_value, RAW_LIGHT_KEY)
