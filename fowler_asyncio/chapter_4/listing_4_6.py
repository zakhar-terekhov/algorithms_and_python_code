# конкурентное выполнение запросов с помощью gather
import asyncio
import aiohttp
from chapter_04 import fetch_status
from util import async_timed


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
            "https://www.goodfon.ru/", 
            "ps://www.goodfon.ru/"
            ]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(
            *requests, return_exceptions=True
        )  # при выполнении сопрограммы исключения не возбуждаются, а возвращаются в списке с результатами
        print(status_codes)


asyncio.run(main())
