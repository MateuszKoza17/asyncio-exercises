import asyncio


async def monitoring() -> None:
    try:
        while True:
            print("Monitoring started...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Monitoring cancelled")


async def measurement(name: str, duration: int) -> str:
    print(f"Starting measurement: {name}")
    await asyncio.sleep(duration)
    return f"{name}: OK"


async def main():
    task_monitoring = asyncio.create_task(monitoring())

    task1 = asyncio.create_task(measurement("Task1", 2))
    task2 = asyncio.create_task(measurement("Task2", 3))
    task3 = asyncio.create_task(measurement("Task3", 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(f"{result1}, {result2}, {result3}")

    task_monitoring.cancel()


asyncio.run(main())
