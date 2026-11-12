import asyncio
import random


async def pagination(page_count: int = 5):
    # Twój async generator tutaj
    pass


async def main():
    async for page in pagination(5):
        print(f"Page {page['page']}: {page['data']}")


asyncio.run(main())

