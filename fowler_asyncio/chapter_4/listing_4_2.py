# отправка веб-запроса с помощью aiohttp
import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://www.google.com"
        status = await fetch_status(session, url)
        print(status)


asyncio.run(main())
