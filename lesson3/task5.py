BREAK_WORD = 'q'


def calc_sum(new_list):
    """ Возвращает сумму чисел списка.
     int для чисел с дробной частью, равной 0, иначе float
     """
    sum = 0
    for item in new_list:
        try:
            sum += float(item)
        except ValueError:
            continue

    return int(sum) if 0 == sum % 1 else sum


total = 0
while True:
    new_list = input(f'Введите числа через пробел. Для выхода введите {BREAK_WORD}: ').split()
    new_sum = calc_sum(new_list)
    total += new_sum
    if BREAK_WORD in new_list:
        print(total)
        break
    else:
        print(f'{new_sum}({total})')
