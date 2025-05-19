# отмена работающих запросов при возникновении исключения
import asyncio
import logging
import aiohttp
from chapter_04 import fetch_pending_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://www.goodfon.ru/"
        fetchers = [
            asyncio.create_task(fetch_pending_status(session, url,5)),
            asyncio.create_task(fetch_pending_status(session, url,1)),
            asyncio.create_task(fetch_pending_status(session, "h://www.goodfon.ru/",2))
        ]

        done, pending = await asyncio.wait(
            fetchers, return_when=asyncio.FIRST_EXCEPTION
        )

        print(f"Завершившиеся задачи: {done}")
        print(f"Ожидающие задачи: {pending}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("Возникло исключение", exc_info=done_task.exception())

        for pending_task in pending: # снятие ожидающих задач
            pending_task.cancel()


asyncio.run(main())
