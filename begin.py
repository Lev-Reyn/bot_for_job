"""перед первым запуском бота запускаем данный код, что бы он создал необходимые файлы"""
import os
import json
if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists('data/baza_for_registration.json'):
    with open('data/baza_for_registration.json', 'w') as file:
        json.dump([], file, indent=4)

