"""
Асинхронность на практике
Цель: приобрести навык использования асинхронного запуска функций на практике
"""
import asyncio

ATLAS_BALLS = 5
strongman_1 = ['Вася', 3]
strongman_2 = ['Петя', 5]
strongman_3 = ['Саня', 10]


async def start_strongman(name: str, power: int):
    print(f'Силач {name} начал соревнования')
    for i in range(0, ATLAS_BALLS):
        await asyncio.sleep(10 // power)
        print(f'Силач {name} поднял {i}-ый шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():

    task_1 = asyncio.create_task(start_strongman(*strongman_1))
    task_2 = asyncio.create_task(start_strongman(*strongman_2))
    task_3 = asyncio.create_task(start_strongman(*strongman_3))
    await task_1
    await task_2
    await task_3


if __name__ == "__main__":
    asyncio.run(start_tournament())