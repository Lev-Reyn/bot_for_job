from aiogram import types


button_help = types.KeyboardButton("/help")
button_registration = types.KeyboardButton('/registration')

keyboardStart = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardStart.add(button_help)
keyboardStart.add(button_registration)

