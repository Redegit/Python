phones_list = [
    {'name': 'Ivan', 'city': 'Moscow', 'phones': ['232-19-55', '+7 (916) 230-00-75']},
    {'name': 'Anna', 'city': 'Samara', 'phones': ['200-11-15']},
    {'name': 'Anna', 'city': 'Vologda', 'phones': ['+7 (931) 711-00-75']},
    {'name': 'Nikolay', 'city': 'Moscow', 'phones': ['+7 (916) 778-71-05', '331-66-11', '783-33- 85']},
    {'name': 'Ivan', 'city': 'Moscow', 'phones': ['+7 (916) 205-41-05', '232-19-55']},
    {'name': 'Anna', 'city': 'Samara', 'phones': ['+7 (916) 105-13-56']}
    ]

new_list = {}
for i in phones_list:
    if i['city'] not in new_list.keys():
        new_list[i['city']] = {}
    for p in i['phones']:
        new_list[i['city']][p] = i['name']
print(new_list)
