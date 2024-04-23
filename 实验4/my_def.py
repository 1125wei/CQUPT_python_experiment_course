import math
import time


def my_sleep(s: int):
    time.sleep(s)
    print("睡眠完成")
    return


def my_sqrt(n: int) -> float:
    return math.sqrt(n)


def my_time() -> time:
    return time.time()
