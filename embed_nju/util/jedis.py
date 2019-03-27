# coding=utf-8
import traceback

import redis
import time
import json
# 封装redis的操作，统一数据接口
# 为没有安装redis的用户提供保存到json文件的接口
host = '127.0.0.1'
def get_pool():
    try:
        pool = redis.ConnectionPool(host=host, port=6379, decode_responses=True, max_connections=1000)
        return pool
    except BaseException as e:
        print_redis_error(e)

def print_redis_error(e):
    msg = traceback.format_exc(e)
    print(msg)
    print("redis failed to connect, please check redis config")
    print("now the data would to save into json file only")

def save_data_to_redis(data, key):
    now = int(time.time())
    timeArray = time.localtime(now)
    time_str = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    conn = redis.Redis(connection_pool=get_pool())
    distance_dict = json.dumps(dict(time=time_str, value=data))
    print(key, '===============')
    print(distance_dict)
    conn.rpush(key, str(distance_dict))


def push_raw_data(data, key):
    rdb = redis.Redis(connection_pool=get_pool())
    rdb.lpush(key, data)


def pop_raw_data(key):
    rdb = redis.Redis(connection_pool=get_pool())
    return rdb.rpop(key)

def set_raw_data(data, key):
    rdb = redis.Redis(connection_pool=get_pool())
    return rdb.set(key, data)

def get_raw_data(key):
    rdb = redis.Redis(connection_pool=get_pool())
    return rdb.get(key)

