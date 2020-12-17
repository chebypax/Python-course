my_list = input('Введите значения списка через пробел: ').split()

for i in range(len(my_list)):
    if i % 2 == 0:
        continue
    tmp = my_list[i]
    my_list[i] = my_list[i - 1]
    my_list[i - 1] = tmp

print(my_list)
