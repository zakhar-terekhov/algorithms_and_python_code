# Выполнение кода, пока другие операции работают в фоне
import asyncio
from util import delay


async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(2)
        print("пока я жду, исполняется другой код")


async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second()
    await first_delay
    await second_delay


asyncio.run(main())
