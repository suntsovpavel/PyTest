# 3.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

import random

n = int(input('Введите размер списка: '))
my_list = [random.randint(0,5) for _ in range(n)]
print(f'Список: {my_list}')

my_dict = {}
for elem in my_list:
    if elem in my_dict:
        my_dict[elem] += 1
    else:
        my_dict[elem] = 1       
print(f'Словарь: {my_dict}')

max_count = 0
valueKey = 0
for key in my_dict:
    if my_dict[key] > max_count:
        max_count = my_dict[key] 
        valueKey = key
print(f'Элемент {valueKey} встречается максимальное количество раз: {max_count}')        