import asyncio
import aiohttp


async def fetch_post(session: aiohttp.ClientSession, post_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with session.get(url) as response:
        post = await response.json()
        return post
    

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[fetch_post(session, x) for x in range(1, 6)],
        )

        for post in results:
            print(f"Post: id: {post['id']}, title: {post['title']}")

asyncio.run(main())