earnings = int(input('Введите значение выручки фирмы: '))
expenses = int(input('Введите значение издержек фирмы: '))

income = earnings - expenses
if 0 == income:
    print('Фирма работает в ноль')
elif income < 0:
    print(f'Фирма работает в убыток со значением {abs(income)}')
else:
    print(f'Поздравляем, фирма работает c прибылью со значением {income}')
    employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль на 1 сотрудника равна {income / employees:.2f}')
