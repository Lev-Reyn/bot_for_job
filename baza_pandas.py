import pandas as pd

columns = ['id', 'phone', 'mondey time', 'tuesday time', 'Wednesday time', 'Thursday time', 'friday time',
           'Saturday time',
           'Sunday time', 'mondey lesson', 'tuesday lesson', 'Wednesday lesson', 'Thursday lesson', 'friday lesson',
           'Saturday lesson', 'Sunday lesson']

columns = list(map(lambda x: x.lower(), columns))
data = pd.DataFrame(columns=columns,
                    index=['N+79996693821', 'N+79964977218', 'N+79992281057'])  # номера телефонов добавяляем так, что бы была N перед
# номером, так как иначе

# data_schedule['id'][0] = '664295561'

# расматривается значение как число


data['mondey time'][0] = '20:00'
data['mondey lesson'][0] = 'МАТЕМАТИКА'

data['wednesday time'][0] = '16:30'
data['wednesday lesson'][0] = 'ПРОГРАММИРОВАНИЕ'

data['thursday time'][0] = '18:00'
data['thursday lesson'][0] = 'МАТЕМАТИКА'

data['saturday time'][0] = '15:00'
data['saturday lesson'][0] = 'ИНФОРМАТИКА'

data['wednesday time'][1] = '20:00'
data['wednesday lesson'][1] = 'МАТЕМАТИКА'

data['thursday time'][1] = '20:00'
data['thursday lesson'][1] = 'ИНФОРМАТИКА'

# print(data)


print(data)
data.to_csv('data_schedule.csv')

print()
