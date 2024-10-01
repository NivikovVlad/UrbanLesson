"""
Хендлеры обработки сообщений
Цель: написать простейшего телеграм-бота, используя асинхронные функции
"""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import api_key

# api = ''
bot = Bot(token=api_key.api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

