# @Time    : 2020/12/5 12:13 上午
# @Author  : h0rs3fa11
# @FileName: port_scanner.py
# @Software: PyCharm
import asyncio
import socket

DONE = object()
# 异步端口扫描
class PortScanner:
    def __init__(self, target):
        self.target = target

    async def start_master(self, ports, task_queue):
        for p in ports:
            # print(f'[master] send {p}')
            await task_queue.put(p)
        # print('[master] send DONE')
        await task_queue.put(DONE)

    async def start_worker(self, task_queue):
        while True:
            port = await task_queue.get()
            if port == DONE:
                return
            # print(f'Start conroutine {port}')
            try:
                _, writer = await asyncio.open_connection(self.target, port)
                # TODO: add port to redis
                # print(f'{port} is open')
                writer.close()
            except ConnectionRefusedError:
                # print(f'connection refused from port {port}
                pass
            finally:
                # print(f'Finish scan {port}')
                task_queue.task_done()

    async def scan(self, port):
        print(f'Start conroutine {port}')
        try:
            _, writer = await asyncio.open_connection(self.target, port)
            # TODO: add port to redis
            print(f'{port} is open')
            writer.close()
        except ConnectionRefusedError:
            # print(f'connection refused from port {port}
            pass
        finally:
            print(f'Finish scan {port}')

    def scan_single(self, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.target, port))
                print(f'{port} is open')
        except ConnectionRefusedError:
            pass