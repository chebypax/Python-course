correct_password = 'password'

name = input('Your name: ')
password = input(f'{name}, enter password: ')
count = 0

while True:
    if password == correct_password or count == 3:
        break
    password = input('Your password is wrong. Please, try again! ')
    count += 1

print('Good bye!')
