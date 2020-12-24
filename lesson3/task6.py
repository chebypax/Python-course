def is_word_to_add(word):
    for symbol in word:
        if ord(symbol) < 97 or ord(symbol) > 122:
            return False

    return True


def int_func(my_string):
    new_string = []
    my_string = my_string.split()
    for word in my_string:
        if is_word_to_add(word):
            new_string.append(word.title())

    return ' '.join(new_string)


new_string = input('Введите предложение: ')
print(int_func(new_string))
