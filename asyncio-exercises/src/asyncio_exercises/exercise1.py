import asyncio


async def greeting() -> None:
    print("Start")
    await asyncio.sleep(2)
    print("Hello after 2 seconds!")


asyncio.run(greeting())
