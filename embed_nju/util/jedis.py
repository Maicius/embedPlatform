# coding=utf-8
import traceback

import redis

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

