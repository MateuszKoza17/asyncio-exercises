import asyncio


async def fetch_users() -> list[str]:
    print("Fetching...")
    await asyncio.sleep(2)
    return ["Anna", "Jan"]


async def fetch_products() -> list[str]:
    print("Fetching...")
    await asyncio.sleep(3)
    return ["Laptop", "Mouse"]


async def fetch_orders() -> list[str]:
    print("Fetching...")
    await asyncio.sleep(1)
    return ["ZAM-001", "ZAM-002"]


async def main():
    start = asyncio.get_running_loop().time()
    await asyncio.gather(
        fetch_orders(),
        fetch_products(),
        fetch_users(),
    )
    print(f"Total time: {asyncio.get_running_loop().time() - start:.1f}s")


asyncio.run(main())
