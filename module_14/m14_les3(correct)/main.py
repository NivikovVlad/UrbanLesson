"""
Доработка бота
Цель: подготовить Telegram-бота для взаимодействия с базой данных
"""

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from module_14.api_key import api
from keyboards import *
# from config import *
# from About_goods import *
import config
import About_goods


# api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

formula = '10 * weight + 6.25 * growth - 5 * age + 5'


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer(f'Привет {message.from_user.username}!\n'
                         f'Выбери опцию', reply_markup=start_kb)


@dp.message_handler(text=['Информация'])
async def info_for_bot(message):
    await message.answer(About_goods.about)


@dp.message_handler(text=['Рассчитать'])
async def calc_(message):
    await message.answer('Выберите опцию', reply_markup=calc_kb)


@dp.message_handler(text=['Купить'])
async def get_buying_list(message):
    for key, value in config.price.items():
        with open(value[0], 'rb') as img:
            await message.answer_photo(img, f'Название: {key} | Описание: {value[1]} | Цена: {value[2]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=shop_kb)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer(formula)
    await call.answer()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.callback_query_handler(text=['back_to_shop'])
async def back_to_shop(call):
    await call.message.answer('Отступаем к прилавкам!', reply_markup=shop_kb)
    await call.message.delete()
    await call.answer()


@dp.callback_query_handler(text=['product_buying'])
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.callback_query_handler(text=['back_to_main_menu'])
async def back_to_main(call):
    await call.message.answer('Отступаем в начало!', reply_markup=start_kb)
    await call.message.delete()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_sex(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой пол(м/ж):')
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_growth(message, state):
    await state.update_data(sex=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    if data['sex'] == 'м':
        calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
    else:
        calories = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161
    await message.answer(f'Необходимо калорий: {calories}')
    await state.finish()



@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)