# @Time    : 2021/1/24 8:43 下午
# @Author  : h0rs3fa11
# @FileName: tools.py
# @Software: PyCharm
from functools import wraps
import time


def time_counter(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = function(*args, **kwargs)
        spent = time.perf_counter() - t0
        print(f'Function {function.__name__} spent time {spent}')
        return res

    return wrapper


def async_time_counter(function):
    @wraps(function)
    async def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = await function(*args, **kwargs)
        spent = time.perf_counter() - t0
        print(f'Function {function.__name__} spent time {spent}')
        return res

    return wrapper
