import asyncio
from func import delay


async def main_1():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, timeout=1)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Time-out')
        print(f'Task was canceled? {delay_task.cancelled()}')


async def main_2():
    task = asyncio.create_task(delay(10))
    try:
        result = await asyncio.wait_for(asyncio.shield(task), 5)
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('задача заняла более 5 сек, будет снята')
        result = await task
        print(result)


if __name__ == '__main__':
    asyncio.run(main_1())
    print('#########################')
    asyncio.run(main_2())
