# 4.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
# Реализовать в один проход цикла

import random

n = int(input('Введите размер списка: '))
arr = [random.randint(1,100) for _ in range(n)]
print(f'Список: {arr}')

if arr[0] > arr[1]:
    firstMax = arr[0]
    secondMax = arr[1]
else:
    firstMax = arr[1]  
    secondMax = arr[0]
for i in range(2,n):
    if arr[i] > firstMax:
        secondMax = firstMax
        firstMax = arr[i]
    if arr[i] < firstMax and arr[i]  > secondMax:
        secondMax = arr[i]    
print(f'firstMax = {firstMax}')
print(f'secondMax = {secondMax}')



