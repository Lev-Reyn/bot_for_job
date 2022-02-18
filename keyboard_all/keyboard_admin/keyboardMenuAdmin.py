from aiogram import types

inl_button_change_the_schedule = types.InlineKeyboardButton('изменить расписание', callback_data='change_the_schedule')
inl_button_tutors_schedule = types.InlineKeyboardButton('моё расписание сегодня', callback_data='tutors_schedule')
inl_button_earnings_today = types.InlineKeyboardButton('заработок сегодня', callback_data='earnings_today')
inl_button_earnings_per_week = types.InlineKeyboardButton('заработок за неделю', callback_data='earnings_per_week')
inl_button_fill_in_the_schedule = types.InlineKeyboardButton('заполнить расписание',
                                                             callback_data='fill_in_the_schedule')
keyboardMenuAdmin = types.InlineKeyboardMarkup()

keyboardMenuAdmin.add(inl_button_change_the_schedule)
keyboardMenuAdmin.insert(inl_button_tutors_schedule)
keyboardMenuAdmin.add(inl_button_earnings_today)
keyboardMenuAdmin.insert(inl_button_earnings_per_week)
keyboardMenuAdmin.add(inl_button_fill_in_the_schedule)

