import asyncio
from asyncio import CancelledError
from func import delay


async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0

    while not long_task.done():
        print('Task have not finished yet. We check in after 1 sec')
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
    except CancelledError:
        print('Task is finished')

if __name__ == '__main__':
    asyncio.run(main())