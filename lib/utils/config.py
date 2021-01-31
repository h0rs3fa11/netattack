# @Time    : 2021/1/31 7:30 下午
# @Author  : h0rs3fa11
# @FileName: config.py
# @Software: PyCharm
from redis import StrictRedis

class Config:
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    redis_store = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)