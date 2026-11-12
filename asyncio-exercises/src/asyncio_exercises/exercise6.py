import asyncio
import random


async def simulate_request(url: str) -> str:
    duration = random.uniform(0.5, 3.0)
    await asyncio.sleep(duration)
    return f"Dane z {url} (czas: {duration:.1f}s)"


async def fetch_with_limit(url: str, timeout: float) -> str | None:
    # Użyj asyncio.wait_for() z timeoutem
    # Obsłuż asyncio.TimeoutError
    pass


async def main():
    urls = [f"https: /api.example.com/data/{i}" for i in range(5)]
    results = await asyncio.gather(
        *[fetch_with_limit(url, timeout=1.5) for url in urls]
    )

    for url, result in zip(urls, results):
        status = result if result else "TIMEOUT"
        print(f"{url} > {status}")


asyncio.run(main())
