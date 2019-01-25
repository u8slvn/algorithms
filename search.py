import functools
import time


def time_exec(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.perf_counter()
        result = func(*args, **kw)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f'{func.__name__!r} executed in {run_time:.6f} secs')

        return result

    return wrapper


@time_exec
def binary_search(sample: list, item: str) -> [bool, str]:
    low = 0
    high = len(sample) - 1

    while low <= high:
        mid = round((low + high) / 2)
        candidate = sample[mid]

        if candidate == item:
            return mid

        if candidate < item:
            low = mid + 1

        high = mid - 1

    return None


@time_exec
def classic_search(sample: list, item: str) -> [bool, str]:
    for index, candidate in enumerate(sample):
        if candidate == item:
            return index

    return None
