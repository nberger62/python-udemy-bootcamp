import time
from time import time
from functools import wraps


def speed_test(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums():
    return sum(x for x in range(1000000))

print(sum_nums())
