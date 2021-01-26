# @Time    : 2020/12/5 12:13 上午
# @Author  : h0rs3fa11
# @FileName: port_scanner.py
# @Software: PyCharm
import os
from multiprocessing import Pool, cpu_count
import socket
import asyncio


class PortScanner:
    def __init__(self, ip, start_port, end_port):
        self.ip = ip
        self.start_port = start_port
        self.end_port = end_port

    def run(self):
        for p in range(self.start_port, self.end_port):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((self.ip, p))
                    print(f'{p} is open')
            except ConnectionRefusedError:
                pass


class ProcessScan:
    def __init__(self, ip, start, end):
        super().__init__()
        self.ip = ip
        self.start = start
        self.end = end

    @staticmethod
    def do_scan(ip, start, end):
        for p in range(start, end):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((ip, p))
                    print(f'{p} is open')
            except ConnectionRefusedError:
                pass

    def run(self):
        cores = cpu_count()
        pool = Pool(cores)
        batches = self.end - self.start + 1
        per_worker = batches // cores
        tasks = list(range(self.start, self.end + 1)[::per_worker])
        if tasks[-1] != self.end:
            tasks.append(self.end)
        for i in range(cores):
            pool.apply_async(ProcessScan.do_scan, (self.ip, tasks[i], tasks[i + 1]))
        pool.close()
        pool.join()


class AsyPortScan:
    def __init__(self, ip, start, end, worker):
        self.ip = ip
        self.start = start
        self.end = end
        self.queue = asyncio.Queue()
        self.worker = worker

    async def generate_tasks(self):
        batches = self.end - self.start + 1
        per_worker = batches // self.worker
        tasks = list(range(self.start, self.end + 1)[::per_worker])
        if tasks[1] != self.end:
            tasks.append(self.end)
        for i in range(len(tasks) - 1):
            await self.queue.put((self.ip, tasks[i], tasks[i + 1]))

    async def scan(self, i):
        while not self.queue.empty():
            host = await self.queue.get()
            # print(host)
            # print(f'scan port range ({host[1]},{host[2] - 1})')
            for p in range(host[1], host[2]):
                conn = asyncio.open_connection(host[0], p)
                try:
                    _, _ = await asyncio.wait_for(conn, timeout=1)
                    print(f'{p} is open')
                except ConnectionRefusedError:
                    pass
                except asyncio.exceptions.TimeoutError:
                    print(f'{host[0]}:{p} timeout')
                    break
                # bug here
                except Exception as e:
                    print(f'unexpect exception occured, {host[0]}:{p}\n{e}')
