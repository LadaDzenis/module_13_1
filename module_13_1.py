import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    ball = 5
    for i in range(ball):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар №{i+1}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Nik', 10))
    task_2 = asyncio.create_task(start_strongman('Vlad', 8))
    task_3 = asyncio.create_task(start_strongman('Mike', 7))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())


