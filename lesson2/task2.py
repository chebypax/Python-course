my_list = input('Введите значения списка через пробел: ').split()

for i in range(1, len(my_list), 2):
    tmp = my_list[i]
    my_list[i] = my_list[i - 1]
    my_list[i - 1] = tmp

print(my_list)
