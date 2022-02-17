"""клавиатура помощи (инлайн клавиатура)"""
from aiogram import types

inl_button_description = types.InlineKeyboardButton('как пользоваться', callback_data='description')  # инлайн кнопка
# по которой будет показываться сообщение с описанием как пользоваться ботом
inl_button_connection_with_the_creator = types.InlineKeyboardButton('связаться с создателем',
                                                                    callback_data='connection_with_the_creator')
inl_button_git_hub = types.InlineKeyboardButton('git hub', callback_data='git_hub')

keyboardHelp = types.InlineKeyboardMarkup()
keyboardHelp.add(inl_button_description)
keyboardHelp.add(inl_button_git_hub)
keyboardHelp.add(inl_button_connection_with_the_creator)
