# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input('Введите размер массива: '))
min = int(input('Введите границы диапазона: '))
max = int(input())
arr = [random.randint(1,100) for _ in range(n)]
print(f'Исходный массив:\n{arr}')
result = {}
for i in range(n):
    if arr[i] >= min and arr[i] <= max:
        result[i] = arr[i]

print(f'Индексы и значения:\n{result}')        
