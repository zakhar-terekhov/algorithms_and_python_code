# использование as_completed
import asyncio
import aiohttp
from chapter_04 import fetch_pending_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = [
            fetch_pending_status(session, "https://www.goodfon.ru/", 2),
            fetch_pending_status(session, "https://www.goodfon.ru/", 1),
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


asyncio.run(main())
