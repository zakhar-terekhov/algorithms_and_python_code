import asyncio
from aiohttp import ClientSession
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status

@async_timed()
async def fetch_pending_status(session: ClientSession, url: str, delay: int) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status