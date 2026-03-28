import asyncio
async def work():
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
        print("Task cancelled")

async def main():
    task = asyncio.create_task(work())
    await asyncio.sleep(1)
    task.cancel()

asyncio.run(main())