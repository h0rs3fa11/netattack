# @Time    : 2020/12/23 10:09 下午
# @Author  : h0rs3fa11
# @FileName: address.py
# @Software: PyCharm
from random import randint

def random_ip():
    ip = f'{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}'
    return ip

def random_port():
    port = randint(1024, 65535)
    return port