# Async IO in python

import asyncio

async def my_async_func():
    await asyncio.sleep(1)
    return "Hello"

async def main():
    result = await my_async_func()
    print(result)

asyncio.run(main())

async def gather_results():
    L = await asyncio.gather(
        my_async_func(),
        my_async_func(),
        my_async_func()
    )
    print(L)

asyncio.run(gather_results())