count = 1
data = list()

while True:
    input_data = input('Введите инфо о товаре в таком формате: '
                       'название: компьютер, цена: 20000, количество: 5, eд: шт.. '
                       'Для выхода введите -1: ')
    if input_data == '-1':
        break

    input_data = input_data.replace(' ', '').replace('\'', '')
    input_data = input_data.replace('"', '').replace('“', '').replace('”', '')
    input_data = input_data.split(',')
    new_set = {}

    for item in input_data:
        new_set[item.split(':')[0]] = item.split(':')[1]

    new_elem = (count, dict(new_set))
    data.append(new_elem)
    count += 1

result = {}
for idx, item in data:
    for key in item:
        new_value = item.get(key)
        if key in result.keys() and new_value not in result.get(key):
            result.get(key).append(new_value)
        else:
            result[key] = [new_value]

print(result)
