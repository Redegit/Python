def match_index(i):
    for j in range(len(new_list)):
        if new_list[j]['name'] == i['name'] and new_list[j]['city'] == i['city']:
            return j
    return None


phones_list = [
    {'name': 'Ivan', 'city': 'Moscow', 'phones': ['232-19-55', '+7 (916) 230-00-75']},
    {'name': 'Anna', 'city': 'Samara', 'phones': ['200-11-15']},
    {'name': 'Anna', 'city': 'Vologda', 'phones': ['+7 (931) 711-00-75']},
    {'name': 'Nikolay', 'city': 'Moscow', 'phones': ['+7 (916) 778-71-05', '331-66-11', '783-33- 85']},
    {'name': 'Ivan', 'city': 'Moscow', 'phones': ['+7 (916) 205-41-05', '232-19-55']},
    {'name': 'Anna', 'city': 'Samara', 'phones': ['+7 (916) 105-13-56']}
    ]
new_list = []

for i in phones_list:
    index = match_index(i)
    if index is None:
        new_list.append(i)
    else:
        new_list[index]['phones'].extend(i['phones'])

[print(i) for i in new_list]
