def my_func(num_1, num_2, num_3):
    new_list = [num_1, num_2, num_3]
    new_list.remove(min(new_list))

    return sum(new_list)


print(my_func(2, 2, 3))
