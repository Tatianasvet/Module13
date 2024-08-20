import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for boll in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {boll} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    number_1 = asyncio.create_task(start_strongman('Стас', 3))
    number_2 = asyncio.create_task(start_strongman('Глеб', 4))
    number_3 = asyncio.create_task(start_strongman('Рома', 5))
    await number_1
    await number_2
    await number_3

asyncio.run(start_tournament())
