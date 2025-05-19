# декоратор для хронометража сопрограмм
import functools
import time
from typing import Callable, Any


def async_timed():
    def wraper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"Выполняется {func} с аргументами {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"{func} завершилась за {total:.4f} сек.")

        return wrapped

    return wraper
