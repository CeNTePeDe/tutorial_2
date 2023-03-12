import asyncio


async def delay(delay_seconds: int) -> int:
    print(f'Я засыпаю на {delay_seconds} минут')
    await asyncio.sleep(delay_seconds)
    print(f'Сон в течение {delay_seconds} закончился')
    return delay_seconds
