my_list = input('Введите слова, разделенные пробелами: ').split()

for i, item in enumerate(my_list, 1):
    print(f'{i} - {item[:10]}')

