number = int(input('Please, enter a positive integer: '))

max_digit = 0
while number > 0:
    tmp = number % 10
    if tmp > max_digit:
        max_digit = tmp
    number = number // 10

print(f'Maximum digit is {max_digit}')
