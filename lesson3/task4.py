def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= 1 / x

    return result


while True:
    try:
        base = float(input('Введите действительное положительное основание степени: '))
        if base <= 0:
            raise ValueError
        break
    except ValueError:
        print('Введено неправильное значение!')

while True:
    try:
        pow_rate = int(input('Введите целый отрицательный показатель степени: '))
        if pow_rate >= 0:
            raise ValueError
        break
    except ValueError:
        print('Введено неправильное значение!')

print(my_func(base, pow_rate))
