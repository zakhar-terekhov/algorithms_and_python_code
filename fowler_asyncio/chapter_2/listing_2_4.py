# использование await для ожидания результата сопрограммы
import asyncio


async def coroutine_add_one(number: int) -> int:
    return number + 1


async def main():
    one_plus_one = await coroutine_add_one(1)
    one_plus_two = await coroutine_add_one(2)
    print(one_plus_one)
    print(one_plus_two)


asyncio.run(main())
