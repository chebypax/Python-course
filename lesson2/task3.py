season = ('winter ' * 2 + 'spring ' * 3 + 'summer ' * 3 + 'autumn ' * 3 + 'winter').split()
dist = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

num = int(input('Введите число от 1 до 12: '))
while num < 1 or num > 12:
    num = int(input('Введенное число должно быть от 1 до 12! Повторите ввод: '))

result = f'Введен месяц {dist.get(num)}, это сезон {season[num - 1]}'

print(result)
