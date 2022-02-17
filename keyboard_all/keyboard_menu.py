"""инлайн кнопки меню"""
from aiogram import types

inl_button_schedule = types.InlineKeyboardButton('Расписание на этой неделе', callback_data='schedule')  # инлайн
# кнопка расписания
inl_button_number_phone_student = types.InlineKeyboardButton('мой номер', callback_data='number_phone_student')
inl_button_home_work = types.InlineKeyboardButton('ДЗ', callback_data='home_work')
inl_button_help = types.InlineKeyboardButton('помощь', callback_data='help_inl')

keyboardMenu = types.InlineKeyboardMarkup().add(inl_button_schedule).add(inl_button_number_phone_student)
keyboardMenu.insert(inl_button_home_work).insert(inl_button_help)
