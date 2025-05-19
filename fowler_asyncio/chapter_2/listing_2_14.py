# основы будущих объектов
from asyncio import Future

my_future = Future()

print(f"Объект готов ? {my_future.done()}")
print(f"Какой резульат хранится в my_future: {my_future.result()}")

my_future.set_result(42)

print(f"Объект готов ? {my_future.done()}")

print(f"Какой резульат хранится в my_future: {my_future.result()}")