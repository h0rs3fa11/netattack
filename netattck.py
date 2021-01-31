# @Time    : 2020/12/4 11:39 下午
# @Author  : h0rs3fa11
# @FileName: netattck.py
# @Software: PyCharm
from lib.core.port_scanner import AsyPortScan, ProcessScan, PortScanner
import asyncio
from lib.utils.tools import async_time_counter, time_counter

WORKERS = 10

def start():
    # processmain()
    asyncio.run(main())
    # singlescan()

@async_time_counter
async def main():
    scanner = AsyPortScan('192.168.220.79', 1, 65535, WORKERS)
    tasks = [asyncio.create_task(scanner.generate_tasks())]
    tasks.extend(asyncio.create_task(scanner.scan(i)) for i in range(WORKERS))
    await asyncio.gather(*tasks)


@time_counter
def processmain():
    ProcessScan('192.168.220.79', 1, 65535).run()

@time_counter
def singlescan():
    PortScanner('127.0.0.1', 1, 60000).run()

if __name__ == '__main__':
    start()
