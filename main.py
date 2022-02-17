import json
import random
import os.path
from config import token, namebot1, namebot2
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import time
import pandas as pd
from keyboard_all.keyboard_start import keyboardStart  # клавиатура старта
from keyboard_all.keyboard_menu import keyboardMenu  # клавиатура меню
from keyboard_all.keyboard_help import keyboardHelp  # клавиатура помощи и связи со мной
from keyboard_all.delatr_message import delete_message  # удаляет сообщения бота через какое-то время
import asyncio

bot = Bot(token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# в keyboard_all.keyboard_start.py есть keyboardStart (это меню старта)

button_registration_phone = types.KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
button_menu = types.KeyboardButton('/menu')


@dp.message_handler(commands=['start'])
async def start_process_command(message: types.Message):
    """начало работы бота"""
    await message.delete()
    await bot.send_message(message.from_user.id, 'пока что просто старт, бот для расписания, \n для того что бы '
                                                 'пользоваться бьотом, необходимо что бы владелец бота внёс вас '
                                                 'в базу и вы подтвердили телефон',
                           reply_markup=keyboardStart)


@dp.message_handler(commands=['help'])
async def help_process_commands(message: types.Message):
    """помощь, описывает, что делает бот (нужно дописать его по окончанию работы)"""
    await message.delete()
    msg = await bot.send_message(message.from_user.id, 'помогаю')
    asyncio.create_task(delete_message(msg, 5))
    time.sleep(1)
    msg_2 = await bot.send_message(message.from_user.id, 'помог!')
    asyncio.create_task(delete_message(msg_2, 5))


@dp.message_handler(commands='registration')
async def registration_process_commands(message: types.Message):
    """даём кнопку на отправку номера телефона, что бы в дальнейшесм его проверить"""
    await message.delete()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(button_registration_phone)
    await bot.send_message(message.from_user.id, 'оправьте свой номер телефона нажимая на кнопку, я проверю '
                                                 'есть ли вы в базе', reply_markup=keyboard)


@dp.message_handler(content_types=['contact'])
async def registratinon_get_number_phone(message: types.Message):
    """проверяет есть ли номер телефона в базе"""
    await message.delete()
    with open('data/baza_for_registration.json', 'r') as file:
        baza_for_registration = json.load(file)
        print(baza_for_registration)
    if f'+{message.contact["phone_number"]}' in baza_for_registration:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(button_menu)

        data = pd.read_csv('data_schedule.csv', encoding='UTF-8', index_col=0)  # открываем что бы закинуть id userА
        print(data)
        await bot.send_message(message.from_user.id, f'ваш номер телефона +{message.contact["phone_number"]} '
                                                     f'подтверждён', reply_markup=keyboard)
        #  дальше закидываем id в data и сохраняем изменённый файл
        row = f'N+{message.contact["phone_number"]}'  # получаем строку, у нас строки N(номер телефона)
        data['id'][row] = f'ID{message.from_user.id}'
        # print(data)
        data.to_csv('data_schedule.csv')  # сохраняем id пользователя
    else:

        await bot.send_message(message.from_user.id, 'вас нет в базе', reply_markup=keyboardStart)


@dp.message_handler(commands=['menu'])
async def menu_process_command(message: types.Message):
    """здесь должны быть инлайн кнопки, которые выдают меню (что умеет делать бот)"""
    data = pd.read_csv('data_schedule.csv', encoding='UTF-8', index_col=0)
    if f'ID{message.from_user.id}' in list(data.id):
        await message.reply('тебе доступны такие функции как:', reply_markup=keyboardMenu)
    else:
        await bot.send_message(message.from_user.id, 'вас нет в базе', reply_markup=keyboardStart)
    await message.delete()


@dp.callback_query_handler(text="schedule")
async def schedule_process_inline(callback_query: types.CallbackQuery):
    """показывает расписание, в разработке"""
    data = pd.read_csv('data_schedule.csv', encoding='UTF-8', index_col=0)
    idx = data[data['id'] == f'ID{callback_query.from_user.id}'].index[0]  # получили индекс строки
    data = data.to_dict()
    # думаю это надо будет вынести в отдельный файл =
    lst_for_schedule = ['mondey lesson', 'mondey time', 'tuesday lesson', 'tuesday time', 'wednesday lesson',
                        'wednesday time', 'thursday lesson', 'thursday time', 'friday lesson', 'friday time',
                        'saturday lesson', 'saturday time', 'sunday lesson', 'sunday time']

    # генерируем сообщение с временем каждого занятия и самим занятием
    for_return = ''
    for i, key_name in enumerate(lst_for_schedule):
        if str(data[key_name][idx]) != 'nan' and i % 2 == 0:
            for_return += '<b>' + key_name[0:-7] + '</b>' + '\n' + data[key_name][idx] + '\n'
        elif str(data[key_name][idx]) != 'nan' and i % 2 != 0:
            for_return += data[key_name][idx] + '\n\n'

    await bot.send_message(callback_query.from_user.id, for_return)
    await callback_query.answer(text='бот находится в разработке, так что не факт, что расписание правдивое',
                                show_alert=True)  # что бы вышло обьявление


@dp.callback_query_handler(text='number_phone_student')
async def number_phone_student_process_inline(callback_query: types.CallbackQuery):
    """показывает номер телефона ученика, вдруг он забыл его (хех)"""
    data = pd.read_csv('data_schedule.csv', encoding='UTF-8', index_col=0)
    idx = data[data['id'] == f'ID{callback_query.from_user.id}'].index  # получаем индекс обьекта в котором данное id
    await bot.send_message(callback_query.from_user.id, f'это именно твой номер!!!\nа вдруг ты его забыл/а\n'
                                                        f'{idx[0].replace("N", "")}')
    await callback_query.answer(text='не знаю для чего я это сделал')


@dp.callback_query_handler(text='home_work')
async def home_work_process_inline(callback_query: types.CallbackQuery):
    """домашнее задание будет показывать, ещё в разраьотке"""
    await callback_query.answer(text='в разработке', show_alert=True)


@dp.callback_query_handler(text='help_inl')
async def help_process_inline(callback_query: types.CallbackQuery):
    """помощь, сдесь можно выдвинуть три кнопки, первая прочитать как пользоваться ботом, вторая мой контакт,
    третья - мой гит хаб"""
    await callback_query.message.delete_reply_markup()
    await bot.send_message(callback_query.from_user.id, 'прежде чем писать мне, почитай как пользоваться ботом',
                           reply_markup=keyboardHelp)


executor.start_polling(dp)
