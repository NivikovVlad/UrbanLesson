from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')]
    ],
    resize_keyboard=True
)

shop_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Завтрак', callback_data='product_buying'),
         InlineKeyboardButton(text='Обед', callback_data='product_buying'),
         InlineKeyboardButton(text='Ужин', callback_data='product_buying'),
         InlineKeyboardButton(text='Комплекс', callback_data='product_buying'),
         InlineKeyboardButton(text='Назад', callback_data='back_to_main_menu')]
    ],
    resize_keyboard=True
)

# by_kb = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text='Купить', callback_data='buy')],
#         [InlineKeyboardButton(text='Назад', callback_data='back_to_shop')]
#     ],
#     resize_keyboard=True
# )


calc_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')],
        [InlineKeyboardButton(text='Назад', callback_data='back_to_start')]
    ],
    resize_keyboard=True
)
