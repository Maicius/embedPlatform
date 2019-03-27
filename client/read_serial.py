import serial
from embed_nju.util.jedis import get_pool
import redis
from embed_nju.util.constant import RAW_DISTANCE_KEY, RAW_TEMPERATURE_KEY, RAW_LIGHT_KEY
def read_serial():
    with serial.Serial('/dev/tty', 9600) as ser:
        while True:
            data = ser.readline().decode()
            if data is not None:
                save_raw_to_redis(data)


def save_raw_to_redis(data):
    conn = redis.Redis(connection_pool=get_pool())
    data = data.split(':')
    data_type = data[0]
    data_value = data[1]
    if data_type == 'temperature':
        conn.set(RAW_TEMPERATURE_KEY, data_value)
    elif data_type == 'distance':
        conn.set(RAW_DISTANCE_KEY, data_value)
    elif data_type == 'light':
        conn.set(RAW_LIGHT_KEY, data_value)
