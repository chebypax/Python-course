run_result = float(input('Введите результат первого забега: '))
goal = float(input('Введите желаемый результат: '))

count = 1
while run_result < goal:
    run_result *= 1.1
    count += 1

print(f'На {count} день спортсмен достиг результата - не менее {goal} км, a именно {run_result:.2f} км')
