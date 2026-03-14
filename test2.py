import asyncio

async def f():
    print("done")
    await asyncio.sleep(3)
    print("done")

asyncio.run(f())