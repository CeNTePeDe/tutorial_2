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
    print(type(sleep_for_three))
    result = await sleep_for_three
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
