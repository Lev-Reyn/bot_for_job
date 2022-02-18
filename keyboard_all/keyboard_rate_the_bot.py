"""клавиатура для оценки бота"""
from aiogram import types

# Здесь хранятся пользовательские данные.
# Т.к. это словарь в памяти, то при перезапуске он очистится
user_data = {}


def get_keyboard_rate_the_bot():
    """функция, которая возвращает клавиатуру для увеличения или уменьшения оценки боту """
    buttons = [
        types.InlineKeyboardButton(text='-1', callback_data='num_minus'),
        types.InlineKeyboardButton(text='+1', callback_data='num_plus'),
        types.InlineKeyboardButton(text='Отправить', callback_data='num_sendNum')
    ]
    keyboardRateTheBot = types.InlineKeyboardMarkup(row_width=2)  # что бы на одной строке было только 2 кнопки
    keyboardRateTheBot.add(*buttons)
    return keyboardRateTheBot


async def update_num_text(message: types.Message, new_value: int):
    """общая функция для для отправления текств с отправкой той же клавиатуры"""
    await message.edit_text(f'Ваша оценка этому боту {new_value}', reply_markup=get_keyboard_rate_the_bot())
