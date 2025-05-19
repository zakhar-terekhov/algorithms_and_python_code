# задание тайм-аутов для сеанса и запросов
import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    total_mills = aiohttp.ClientTimeout(total=0.01)
    async with session.get(url, timeout=total_mills) as result:
        return result.status


async def main():
    session_mills = aiohttp.ClientTimeout(total=1, connect=0.1)
    async with aiohttp.ClientSession(timeout=session_mills) as session:
        url = "https://www.google.com"
        status = await fetch_status(session, url)
        print(status)


asyncio.run(main())
