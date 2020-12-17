my_list = input('Введите слова, разделенные пробелами: ').split()

for i, item in enumerate(my_list):
    print(f'{i + 1} - {item[:10]}')

