import asyncio


async def greeting():
    print("Start")
    await asyncio.sleep(2)
    print("Hello after 2 seconds!")


asyncio.run(greeting())
