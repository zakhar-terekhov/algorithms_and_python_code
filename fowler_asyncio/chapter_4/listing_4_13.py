# обработка результатов по мере поступления
import asyncio
import logging
import aiohttp
from chapter_04 import fetch_pending_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://www.goodfon.ru/"
        pending = [
            asyncio.create_task(fetch_pending_status(session, url, 5)),
            asyncio.create_task(fetch_pending_status(session, url, 1)),
            asyncio.create_task(fetch_pending_status(session, "h://www.goodfon.ru/", 2)),
        ]

        while pending:
            done, pending = await asyncio.wait(
                pending, return_when=asyncio.FIRST_COMPLETED
            )

            print(f"Завершившиеся задачи: {len(done)}")
            print(f"Ожидающие задачи: {len(pending)}")

            for done_task in done:
                if done_task.exception() is None:
                    print(done_task.result())
                else:
                    logging.error("Возникло исключение", exc_info=done_task.exception())


asyncio.run(main())
