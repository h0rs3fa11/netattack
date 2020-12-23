# @Time    : 2020/12/4 11:39 下午
# @Author  : h0rs3fa11
# @FileName: netattck.py
# @Software: PyCharm
import time
from multiprocessing import Pool

from lib.core.port_scanner import PortScanner

p = PortScanner('127.0.0.1')

def scan_port():
    [p.scan_single(port) for port in range(1, 2000)]

def syn_flood():
    pass

if __name__ == '__main__':
    with Pool(1) as process:
        process.apply(scan_port)
