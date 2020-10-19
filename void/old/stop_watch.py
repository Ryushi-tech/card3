from functools import wraps
import time


def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = (time.time() - start) * 1000
        print(f"{func.__name__}: {elapsed_time:.3f} ms")
        return result

    return wrapper
