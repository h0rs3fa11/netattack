# @Time    : 2020/12/4 11:39 下午
# @Author  : h0rs3fa11
# @FileName: netattck.py
# @Software: PyCharm
from lib.core.port_scanner import AsyPortScan, ProcessScan, PortScanner
import asyncio

from lib.utils.tools import async_time_counter, time_counter

WORKERS = 5


@async_time_counter
async def main():
    scanner = AsyPortScan('127.0.0.1', 1, 60000, WORKERS)
    tasks = [asyncio.create_task(scanner.generate_tasks())]
    tasks.extend(asyncio.create_task(scanner.scan(i)) for i in range(WORKERS))
    await asyncio.gather(*tasks)


@time_counter
def processmain():
    ProcessScan('127.0.0.1', 1, 60000).run()

@time_counter
def singlescan():
    PortScanner('127.0.0.1', 1, 60000).run()

if __name__ == '__main__':
    # processmain()
    asyncio.run(main())
    # singlescan()
