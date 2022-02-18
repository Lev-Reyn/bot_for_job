"""клавиатура помощи (инлайн клавиатура)"""
from aiogram import types

inl_button_description = types.InlineKeyboardButton('как пользоваться', callback_data='description')  # инлайн кнопка
# по которой будет показываться сообщение с описанием как пользоваться ботом
inl_button_connection_with_the_creator = types.InlineKeyboardButton('связаться с создателем', url='https://t.me/lv_rey',
                                                                    callback_data='connection_with_the_creator')
inl_button_git_hub = types.InlineKeyboardButton('git hub', url='https://github.com/Lev-Reyn/bot_for_job.git',
                                                callback_data='git_hub')
inl_button_rate_the_bot = types.InlineKeyboardButton('оценить бота', callback_data='rate_the_bot')

keyboardHelp = types.InlineKeyboardMarkup()
keyboardHelp.add(inl_button_description)
keyboardHelp.add(inl_button_connection_with_the_creator)
keyboardHelp.add(inl_button_git_hub)
keyboardHelp.insert(inl_button_rate_the_bot)
