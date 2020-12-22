def div_func(num_1, num_2):
    return round(num_1 / num_2, 2)


num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

try:
    print(div_func(num_1, num_2))
except ZeroDivisionError:
    print('На ноль делить нельзя!')
