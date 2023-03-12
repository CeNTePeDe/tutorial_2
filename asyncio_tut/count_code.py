import asyncio
from func import delay, async_timed


@async_timed()
async def cpu_bound_work() -> int:
    counter = 0
    for i in range(10_000_000):
        counter += 1
    return counter


@async_timed()
async def main():
    task_one = asyncio.create_task(cpu_bound_work())
    task_two = asyncio.create_task(cpu_bound_work())
    task_three = asyncio.create_task(delay(3))
    await task_three
    await task_one
    await task_two


if __name__ == '__main__':
    asyncio.run(main())
