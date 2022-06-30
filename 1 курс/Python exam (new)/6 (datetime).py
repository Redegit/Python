import datetime


months = {
    "января": 1,
    "февраля": 2,
    "матра": 3,
    "апреля": 4,
    "мая": 5,
    "июня": 6,
    "июля": 7,
    "августа": 8,
    "сентября": 9,
    "октября": 10,
    "ноября": 11,
    "декабря": 12
}

date = input("Введите дату: ").split()
day = int(date[0])
month = months[date[1]]
year = int(date[2])

date_f = datetime.date(year, month, day)
weekday = date_f.weekday()

dic_week = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}

weekday = dic_week[weekday]
print(weekday)
