"""добавляем номер телефона для регистрации в боте"""
import json

new_phone_of_user = input()
with open('data/baza_for_registration.json') as file:
    baza_for_registration = json.load(file)
lst_with_numbers_phone: list
if len(new_phone_of_user) == 12 and new_phone_of_user[1:].isdigit() and new_phone_of_user[0] == '+':
    baza_for_registration.append(new_phone_of_user)
    print('всё ок')
else:
    print('не добвавился так как не проходит по условиям')
with open('data/baza_for_registration.json', 'w') as file:
    json.dump(list(set(baza_for_registration)), file, indent=4)