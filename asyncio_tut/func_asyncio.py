import asyncio
from func import delay


async def hello_world_message():
    await delay(1)
    return 'Hello world'


async def add_number(number: int) -> int:
    return number + 1


async def add_number_2(number: int) -> int:
    return number + 2


async def main() -> None:
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_again_2 = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_for_three
    await sleep_again_2


if __name__ == '__main__':
    asyncio.run(main())
