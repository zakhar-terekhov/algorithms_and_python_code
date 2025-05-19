# изучение поведения wait по-умолчанию
import asyncio
import logging
import aiohttp
from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, "https://www.goodfon.ru/")),
            asyncio.create_task(fetch_status(session, "h://www.goodfon.ru/")),
        ]

        done, pending = await asyncio.wait(fetchers)

        print(f"Завершившиеся задачи: {done}")
        print(f"Ожидающие задачи: {pending}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error(
                    "Возникло исключение", 
                    exc_info=done_task.exception()
                )


asyncio.run(main())
