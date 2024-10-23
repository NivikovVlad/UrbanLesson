"""
Инлайн клавиатуры
Цель: научится создавать Inline клавиатуры и кнопки на них в Telegram-bot
"""


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from module_13.api_key import api

# api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

formula = '10 * weight + 6.25 * growth - 5 * age + 5'

reply_kb = ReplyKeyboardMarkup(resize_keyboard=True)
button0 = KeyboardButton(text='Рассчитать')
reply_kb.add(button0)
button1 = KeyboardButton(text='Информация')
reply_kb.add(button1)

inline_kb = InlineKeyboardMarkup(resize_keyboard=True)
inline_button0 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inline_kb.add(inline_button0)
inline_button1 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(inline_button1)


@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=inline_kb)


@dp.callback_query_handler(text=['formulas'])
async def get_formulas(call):
    await call.message.answer(formula)
    await call.answer()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


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


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=reply_kb)


@dp.message_handler(text=['Информация'])
async def info_for_bot(message):
    await message.answer('Бот рассчитывает норму калорий ')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)