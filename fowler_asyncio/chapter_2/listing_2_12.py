# Задание тайм-аута (снятия задачи) для задачи с помощью await_for
import asyncio
from util import delay


async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, 1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print("Тайм-аут")
        print(f"Задача была снята? {delay_task.cancelled()}")


asyncio.run(main())
