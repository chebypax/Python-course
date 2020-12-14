number = input('Please, enter a number: ')

count = 1
result = 0
while count <= 3:
    result += int(number * count)
    count += 1

print(result)
