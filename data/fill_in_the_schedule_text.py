from typing import List

fillInTheScheduleText = """<u>adding a student</u>
Номер телефона ученика: 79999999999
Имя ученика| Иван 11 класс ЕГЭ мат, инф
Понедельник|
Вторник|
Среда| прог 20:00
Четверг| мат 13:30
Пятница| инф 15:00
Суббота|
Воскресенье|"""


def adding_a_studentFunc(message_lst: List[str]):
    for i in range(len(message_lst) - 1, -1, -1):
        if message_lst[i].split('|')[1] != '':
            pass
        print('доработать')
