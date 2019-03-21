import traceback

import redis

# 封装redis的操作，统一数据接口
# 为没有安装redis的用户提供保存到json文件的接口
class jedis(object):
    def __init__(self):
        # 使用redis保存数据，如果没有redis须注释掉这两句代码
        # 使用json文件保存数据
        self.data_array = []
        self.host = "127.0.0.1"
        self.port = "6379"
        self.re = self.get_re()

    # 返回一个原生的redis对象
    def get_re(self):
        try:
            pool = redis.ConnectionPool(host=self.host, port=6379, decode_responses=True)
            return redis.StrictRedis(connection_pool=pool)
        except BaseException as e:
            self.print_redis_error(e)

    def connect_redis(self):
        return self.re

    def print_redis_error(self, e):
        msg = traceback.format_exc(e)
        print(msg)
        print("redis failed to connect, please check redis config")
        print("now the data would to save into json file only")