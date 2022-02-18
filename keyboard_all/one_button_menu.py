from aiogram import types

button_menu = types.KeyboardButton('/menu')
keyboardOneButtonMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardOneButtonMenu.add(button_menu)
