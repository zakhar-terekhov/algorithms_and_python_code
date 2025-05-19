# выполнение счетного кода в отладочном режиме
import asyncio


async def cpu_bound_work():
    counter = 0
    for _ in range(10000000):
        counter += 1
    return counter


async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    await task_one


asyncio.run(main(), debug=True)
