# счетный код и длительная задача
import asyncio
from util import async_timed, delay


@async_timed()
async def cpu_bound_work():
    counter = 0
    for _ in range(10000000):
        counter += 1
    return counter


@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    delay_task = asyncio.create_task(delay(4))
    await task_one
    await task_two
    await delay_task


asyncio.run(main())
