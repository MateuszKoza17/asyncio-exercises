import asyncio
import random


async def pagination(page_count: int = 5):
    for i in range(1, page_count + 1):
        await asyncio.sleep(0.5)
        result_data = {"page": i, "data": [random.randint(0, 99) for _ in range(3)]}
        yield result_data


async def main():
    async for page in pagination(5):
        print(f"Page {page['page']}: {page['data']}")


asyncio.run(main())
