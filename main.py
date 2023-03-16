from datetime import datetime, date

users = [
    {'name': 'Alice', 'birthday': datetime(1990, 2, 18)},
    {'name': 'Bob', 'birthday': datetime(1992, 4, 3)},
    {'name': 'Charlie', 'birthday': datetime(1985, 4, 17)},
    {'name': 'David', 'birthday': datetime(1988, 4, 21)},
    {'name': 'Eve', 'birthday': datetime(1983, 4, 22)}
]    

def get_birthdays_per_week(users):
    today = datetime.today().date()
    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    bdays_by_weekday = {
        wday: [] for wday in weekdays.keys()
    }
    future_bdays = []
    for user in users:
        username = user['name']
        user_bday = date(datetime.today().year, user['birthday'].month, user['birthday'].day)
        days_till_bday = (user_bday - today).days
        if days_till_bday > 7:
            future_bdays.append((username, user_bday))
        elif days_till_bday >= 0:
            weekday = user_bday.weekday()
            if weekday in [5, 6]:
                bdays_by_weekday[0].append(f'{username} має ДР {user_bday.strftime("%m.%d")}')
            else:
                bdays_by_weekday[weekday].append(f'{username} має ДР {user_bday.strftime("%m.%d")}')
    if not any(bdays_by_weekday.values()):
        if future_bdays:
            sorted_future_bdays = sorted(future_bdays, key=lambda x: x[1])
            nearest_bday = [(a, b) for a, b in sorted_future_bdays if b == sorted_future_bdays[0][1]]
            names = [n for n, d in nearest_bday]
            names_str = ', '.join(names)
            print(f'На майбутній тиждень, дня народження ні в кого немає! Найближчий ДР {nearest_bday[0][1]} у: {names_str}')
    else:
        for wday, bdays in bdays_by_weekday.items():
            if bdays:
                weekday_name = weekdays[wday]
                print(f'{weekday_name}: {", ".join(bdays)}')


if __name__ == "__main__":
    get_birthdays_per_week(users)