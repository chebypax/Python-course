my_list = [7, 5, 3, 3, 2]

new_elem = int(input('Введите новый элемент списка: '))

for i in range(len(my_list)):
    if new_elem > my_list[i]:
        my_list.insert(i, str(new_elem))
        break

    if i == len(my_list) - 1:
        my_list.append(str(new_elem))

print(my_list)
