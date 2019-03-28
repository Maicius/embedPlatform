from embed_nju.util import constant
from embed_nju.util.jedis import get_pool
import redis
def clear_table():
    conn = redis.Redis(connection_pool=get_pool())
    conn.delete(constant.RAW_DISTANCE_KEY)
    conn.delete(constant.RAW_WET_KEY)
    conn.delete(constant.RAW_LIGHT_KEY)
    conn.delete(constant.RAW_TEMPERATURE_KEY)

    conn.delete(constant.TEMPERATURE_KEY)
    conn.delete(constant.LIGHT_KEY)
    conn.delete(constant.DISTANCE_KEY)
    conn.delete(constant.WET_KEY)

    print("success to clear redis")

if __name__ == '__main__':
    clear_table()